"""Look up Telugu catalog entries in Apple's public iTunes Search API.

Run manually when refreshing the bundled India media index. Nothing runs at app
runtime; only exact title/artist matches are accepted, and previews are used only
when Apple returns a previewUrl for that track.
"""
import json
import re
import time
from pathlib import Path

import requests


ROOT = Path(__file__).parent
CATALOG = ROOT / "indian_catalog.json"
MEDIA = ROOT / "catalog_media.json"
API = "https://itunes.apple.com/search"


def norm(value: str) -> str:
    value = re.sub(r"\([^)]*\)", " ", value.casefold())
    return " ".join(re.findall(r"[a-z0-9]+", value))


def match_score(title: str, artist: str, result: dict) -> int:
    def title_norm(value: str) -> str:
        value = re.sub(r"\s*\(from [^)]*\)", " ", value, flags=re.I)
        value = re.sub(r"\s*\[from [^]]*\]", " ", value, flags=re.I)
        return norm(value)

    requested_title = title_norm(title)
    found_title = title_norm(result.get("trackName", ""))
    if not requested_title or not found_title:
        return -1
    # Reject remixes/covers and other title variants unless that variant was
    # explicitly requested in the catalog.
    if requested_title != found_title:
        return -1
    wanted_artists = {w for w in norm(artist).split() if len(w) >= 4}
    found_artists = {w for w in norm(result.get("artistName", "")).split() if len(w) >= 4}
    overlap = len(wanted_artists & found_artists)
    if overlap == 0:
        return -1
    return overlap


def main():
    songs = json.loads(CATALOG.read_text(encoding="utf-8"))
    media = json.loads(MEDIA.read_text(encoding="utf-8"))
    unique = {}
    for song in songs:
        key = f"{song['title'].casefold()}|{song['artist'].casefold()}"
        unique.setdefault(key, song)

    session = requests.Session()
    session.headers["User-Agent"] = "MoodMix catalog preview lookup/1.0"
    matches = 0
    previews = 0
    failures = []
    for number, (key, song) in enumerate(unique.items(), start=1):
        params = {"term": f"{song['title']} {song['artist']}", "entity": "song", "country": "IN", "limit": 30}
        try:
            response = session.get(API, params=params, timeout=20)
            response.raise_for_status()
            results = response.json().get("results", [])
        except (requests.RequestException, ValueError) as error:
            failures.append((song["title"], str(error)))
            print(f"{number}/{len(unique)} ERROR: {song['title']}", flush=True)
            time.sleep(1.2)
            continue

        candidates = [(match_score(song["title"], song["artist"], result), result) for result in results]
        candidates = [(score, result) for score, result in candidates if score > 0]
        if not candidates:
            failures.append((song["title"], "No exact title and artist match in Apple catalog"))
            print(f"{number}/{len(unique)} no exact match: {song['title']}", flush=True)
        else:
            _, result = max(candidates, key=lambda pair: pair[0])
            entry = {
                "listen_url": result.get("trackViewUrl") or song["listen_url"],
                "artwork_url": result.get("artworkUrl100", "").replace("100x100bb", "600x600bb"),
                "album": result.get("collectionName", ""),
                "source": "Apple iTunes Search catalog",
            }
            if result.get("previewUrl"):
                entry["preview_url"] = result["previewUrl"]
                previews += 1
            media[key] = entry
            matches += 1
            print(f"{number}/{len(unique)} matched{' with preview' if result.get('previewUrl') else ', no preview'}: {song['title']}", flush=True)
        time.sleep(1.2)

    MEDIA.write_text(json.dumps(media, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Finished: {matches}/{len(unique)} exact catalog matches; {previews} official previews; {len(failures)} unresolved.", flush=True)


if __name__ == "__main__":
    main()
