from __future__ import annotations

import os
import re
from html import escape
from dataclasses import asdict, dataclass, field
from typing import Any

import requests
import streamlit as st


st.set_page_config(page_title="MoodMix · Find your feeling", page_icon="♫", layout="wide")

MOODS: dict[str, dict[str, Any]] = {
    "Happy": {"emoji": "☀️", "description": "Bright, buoyant, and full of life.", "profile": {"energy": .78, "valence": .88, "danceability": .72, "tempo": 122, "acousticness": .28, "instrumentalness": .08}},
    "Sad": {"emoji": "🌧️", "description": "Gentle songs for sitting with a feeling.", "profile": {"energy": .28, "valence": .18, "danceability": .32, "tempo": 72, "acousticness": .58, "instrumentalness": .2}},
    "Calm": {"emoji": "🌿", "description": "Soft edges, slow breaths, quiet focus.", "profile": {"energy": .22, "valence": .48, "danceability": .3, "tempo": 76, "acousticness": .72, "instrumentalness": .52}},
    "Romantic": {"emoji": "💗", "description": "Warm melodies and close-to-the-heart songs.", "profile": {"energy": .42, "valence": .62, "danceability": .5, "tempo": 92, "acousticness": .42, "instrumentalness": .12}},
    "Energetic": {"emoji": "⚡", "description": "A pulse that keeps you moving.", "profile": {"energy": .92, "valence": .66, "danceability": .82, "tempo": 138, "acousticness": .12, "instrumentalness": .03}},
    "Focus": {"emoji": "🎧", "description": "Steady, low-distraction listening for deep work.", "profile": {"energy": .38, "valence": .48, "danceability": .36, "tempo": 96, "acousticness": .48, "instrumentalness": .82}},
    "Nostalgic": {"emoji": "📼", "description": "Familiar-feeling melodies with a little distance.", "profile": {"energy": .48, "valence": .52, "danceability": .48, "tempo": 98, "acousticness": .42, "instrumentalness": .16}},
    "Late Night": {"emoji": "🌙", "description": "Unhurried tracks for the hours after dark.", "profile": {"energy": .3, "valence": .38, "danceability": .4, "tempo": 82, "acousticness": .44, "instrumentalness": .32}},
    "Motivational": {"emoji": "🔥", "description": "Forward motion, one track at a time.", "profile": {"energy": .86, "valence": .72, "danceability": .7, "tempo": 128, "acousticness": .16, "instrumentalness": .05}},
    "Dreamy": {"emoji": "☁️", "description": "Floaty textures and a soft sense of wonder.", "profile": {"energy": .3, "valence": .58, "danceability": .34, "tempo": 88, "acousticness": .4, "instrumentalness": .68}},
}

# Query terms are mood descriptors, not genre seeds. Results remain provider-supplied songs.
MOOD_QUERIES = {
    "Happy": ["feel good", "good mood", "joyful"], "Sad": ["heartbreak", "melancholy", "sad"],
    "Calm": ["peaceful", "calm", "unwind"], "Romantic": ["love song", "romantic", "intimate"],
    "Energetic": ["high energy", "get moving", "adrenaline"], "Focus": ["focus", "deep work", "concentration"],
    "Nostalgic": ["nostalgia", "remember when", "throwback feeling"], "Late Night": ["after hours", "late night", "night drive"],
    "Motivational": ["motivation", "keep going", "inspiration"], "Dreamy": ["dreamy", "ethereal", "drifting"],
}

FEATURE_LABELS = {"energy": "Energy", "valence": "Valence", "danceability": "Danceability", "tempo": "Tempo", "acousticness": "Acousticness", "instrumentalness": "Instrumentalness"}


@dataclass
class Track:
    title: str
    artist: str
    album: str = ""
    artwork: str = ""
    preview_url: str = ""
    preview_source: str = ""
    listen_url: str = ""
    source: str = ""
    track_id: str = ""
    features: dict[str, float] = field(default_factory=dict)
    sources: set[str] = field(default_factory=set)
    score: float | None = None
    explanation: str = ""


def _clean(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.casefold())


def _track_key(track: Track) -> tuple[str, str]:
    return _clean(track.title), _clean(track.artist.split(" feat.")[0].split(" featuring ")[0])


def _get_json(url: str, *, params: dict[str, Any] | None = None, headers: dict[str, str] | None = None) -> dict[str, Any]:
    response = requests.get(url, params=params, headers=headers, timeout=12)
    response.raise_for_status()
    return response.json()


@st.cache_data(ttl=900, show_spinner=False)
def search_itunes(term: str, country: str) -> list[dict[str, Any]]:
    payload = _get_json("https://itunes.apple.com/search", params={"term": term, "media": "music", "entity": "song", "limit": 18, "country": country})
    items = []
    for item in payload.get("results", []):
        if not item.get("trackName") or not item.get("artistName"):
            continue
        items.append(asdict(Track(
            title=item["trackName"], artist=item["artistName"], album=item.get("collectionName", ""),
            artwork=item.get("artworkUrl100", "").replace("100x100", "400x400"), preview_url=item.get("previewUrl", ""), preview_source="Apple Music / iTunes" if item.get("previewUrl") else "",
            listen_url=item.get("trackViewUrl", ""), source="Apple Music / iTunes", track_id=str(item.get("trackId", "")),
            features={"tempo": float(item["bpm"])} if item.get("bpm") else {}, sources={"Apple Music / iTunes"},
        )))
    return items


@st.cache_data(ttl=900, show_spinner=False)
def search_deezer(term: str) -> list[dict[str, Any]]:
    payload = _get_json("https://api.deezer.com/search/track", params={"q": term, "limit": 18})
    if payload.get("error"):
        raise requests.HTTPError(f"Deezer returned an API error: {payload['error']}")
    items = []
    for item in payload.get("data", []):
        title, artist = item.get("title"), (item.get("artist") or {}).get("name")
        if not title or not artist:
            continue
        items.append(asdict(Track(
            title=title, artist=artist, album=(item.get("album") or {}).get("title", ""),
            artwork=(item.get("album") or {}).get("cover_xl", ""), preview_url=item.get("preview", ""), preview_source="Deezer" if item.get("preview") else "",
            listen_url=item.get("link", ""), source="Deezer", track_id=str(item.get("id", "")),
            features={"tempo": float(item["bpm"])} if item.get("bpm") else {}, sources={"Deezer"},
        )))
    return items


def spotify_token(client_id: str, client_secret: str) -> str | None:
    if not client_id or not client_secret:
        return None
    try:
        response = requests.post("https://accounts.spotify.com/api/token", data={"grant_type": "client_credentials"}, auth=(client_id, client_secret), timeout=12)
        response.raise_for_status()
        return response.json().get("access_token")
    except requests.RequestException:
        return None


def search_spotify(term: str, token: str) -> list[dict[str, Any]]:
    payload = _get_json("https://api.spotify.com/v1/search", params={"q": term, "type": "track", "limit": 18, "market": "US"}, headers={"Authorization": f"Bearer {token}"})
    items = []
    for item in (payload.get("tracks") or {}).get("items", []):
        artists = item.get("artists") or []
        images = (item.get("album") or {}).get("images") or []
        if not item.get("name") or not artists:
            continue
        items.append(asdict(Track(title=item["name"], artist=artists[0]["name"], album=(item.get("album") or {}).get("name", ""), artwork=images[0].get("url", "") if images else "", preview_url=item.get("preview_url") or "", preview_source="Spotify" if item.get("preview_url") else "", listen_url=(item.get("external_urls") or {}).get("spotify", ""), source="Spotify", track_id=item.get("id", ""), sources={"Spotify"})))
    return items


def spotify_features(ids: list[str], token: str) -> dict[str, dict[str, float]]:
    # Spotify marks this endpoint deprecated and may deny access; treat that as missing data.
    output: dict[str, dict[str, float]] = {}
    for offset in range(0, len(ids), 100):
        batch = ids[offset:offset + 100]
        try:
            payload = _get_json("https://api.spotify.com/v1/audio-features", params={"ids": ",".join(batch)}, headers={"Authorization": f"Bearer {token}"})
            for item in payload.get("audio_features") or []:
                if item and item.get("id"):
                    output[item["id"]] = {key: float(item[key]) for key in FEATURE_LABELS if item.get(key) is not None}
        except requests.RequestException:
            continue
    return output


def merge_tracks(rows: list[dict[str, Any]]) -> list[Track]:
    merged: dict[tuple[str, str], Track] = {}
    for row in rows:
        row["sources"] = set(row.get("sources", []))
        track = Track(**row)
        key = _track_key(track)
        if not all(key):
            continue
        if key not in merged:
            merged[key] = track
            continue
        current = merged[key]
        current.sources.update(track.sources)
        current.features.update({k: v for k, v in track.features.items() if v is not None})
        for field_name in ("artwork", "preview_url", "preview_source", "listen_url", "album", "track_id"):
            if not getattr(current, field_name) and getattr(track, field_name):
                setattr(current, field_name, getattr(track, field_name))
        # Prefer the actual Deezer link / preview if Apple has no preview; keep source attribution.
        if not current.listen_url and track.listen_url:
            current.listen_url, current.source = track.listen_url, track.source
    return list(merged.values())


def rank_tracks(tracks: list[Track], mood: str) -> list[Track]:
    target = MOODS[mood]["profile"]
    weights = {"energy": 1.25, "valence": 1.1, "danceability": .9, "tempo": .75, "acousticness": .65, "instrumentalness": .55}
    for track in tracks:
        available = [(key, track.features[key]) for key in target if key in track.features]
        if not available:
            track.score = None
            track.explanation = "Mood match can’t be scored: this source returned no audio features."
            continue
        total_weight = sum(weights[key] for key, _ in available)
        distance = sum(weights[key] * min(abs(value - target[key]) / (120 if key == "tempo" else 1), 1) for key, value in available) / total_weight
        track.score = round((1 - distance) * 100)
        closest = min(available, key=lambda pair: abs(pair[1] - target[pair[0]]) / (120 if pair[0] == "tempo" else 1))
        key, value = closest
        if key == "tempo":
            track.explanation = f"Its {value:.0f} BPM tempo is close to this mood’s {target[key]} BPM target."
        else:
            descriptor = "high" if value >= .68 else "low" if value <= .32 else "mid-range"
            track.explanation = f"Its {descriptor} {FEATURE_LABELS[key].lower()} ({value:.2f}) fits this mood’s profile."
        if len(available) > 1:
            track.explanation += f" Matched on {len(available)} available audio features."
    return sorted(tracks, key=lambda item: (item.score is None, -(item.score or 0), item.title.casefold()))


def _style() -> None:
    st.markdown("""<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
    :root { --ink:#f4f2ed; --muted:#aaa9b5; --panel:#171720; --line:rgba(255,255,255,.09); --lime:#d5f36a; }
    html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
    .stApp { background: radial-gradient(ellipse at 74% -8%, rgba(126,91,190,.22), transparent 38%), #0d0d12; color:var(--ink); }
    .block-container { max-width:1240px; padding-top:1.35rem; }
    [data-testid="stSidebar"] { background:#111117; border-right:1px solid var(--line); }
    .brand { font:800 1.35rem Manrope,sans-serif; letter-spacing:-.06em; color:#f7f5f0; }
    .brand b { color:var(--lime); }
    .eyebrow { color:#c9d991; font-size:.72rem; font-weight:700; letter-spacing:.16em; text-transform:uppercase; }
    .hero { padding:3.1rem 0 1.4rem; }
    .hero h1 { font:800 clamp(2.7rem,6vw,5.1rem)/.98 Manrope,sans-serif; letter-spacing:-.075em; margin:.7rem 0 1rem; }
    .hero h1 span { color:var(--lime); }
    .hero p { max-width:570px; color:#b1afba; font-size:1.04rem; line-height:1.65; }
    .section-label { color:#aaa9b5; font-size:.75rem; font-weight:700; letter-spacing:.13em; text-transform:uppercase; margin:.35rem 0 .85rem; }
    .song-card { display:flex; gap:16px; padding:14px; min-height:148px; border:1px solid var(--line); border-radius:18px; background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.018)); margin:0 0 14px; }
    .cover { width:112px; height:112px; flex:0 0 112px; object-fit:cover; border-radius:12px; background:#282832; }
    .cover-empty { width:112px; height:112px; flex:0 0 112px; display:grid; place-items:center; border-radius:12px; background:#282832; font-size:2rem; }
    .song-title { font:700 1.02rem Manrope,sans-serif; color:#f4f2ed; margin:3px 0 3px; }
    .song-artist { color:#b0aeb9; font-size:.88rem; }
    .song-album { color:#777681; font-size:.76rem; margin-top:3px; }
    .pills { display:flex; flex-wrap:wrap; gap:6px; margin-top:10px; }
    .pill { border:1px solid rgba(255,255,255,.11); border-radius:99px; padding:4px 8px; color:#d0ced6; font-size:.7rem; }
    .pill-score { border-color:rgba(213,243,106,.28); background:rgba(213,243,106,.09); color:var(--lime); }
    .why { color:#a9a8b1; font-size:.77rem; margin-top:9px; line-height:1.45; }
    .source-note { color:#85838e; font-size:.72rem; margin-top:5px; }
    .stButton > button { border-radius:12px; }
    div[data-testid="stAudio"] { margin-top:5px; }
    </style>""", unsafe_allow_html=True)


def _render_track(track: Track, index: int) -> None:
    safe_artwork = escape(track.artwork, quote=True)
    image = f'<img class="cover" src="{safe_artwork}" alt="Album artwork">' if track.artwork else '<div class="cover-empty">♫</div>'
    score = f'<span class="pill pill-score">{track.score}% mood match</span>' if track.score is not None else '<span class="pill">Audio features unavailable</span>'
    energy = f'<span class="pill">Energy {track.features["energy"]:.2f}</span>' if "energy" in track.features else '<span class="pill">Energy unavailable</span>'
    bpm = f'<span class="pill">{track.features["tempo"]:.0f} BPM</span>' if "tempo" in track.features else '<span class="pill">BPM unavailable</span>'
    extra_features = "".join(f'<span class="pill">{FEATURE_LABELS[key]} {track.features[key]:.2f}</span>' for key in ("valence", "danceability", "acousticness", "instrumentalness") if key in track.features)
    details = f'<div class="song-title">{escape(track.title)}</div><div class="song-artist">{escape(track.artist)}</div><div class="song-album">{escape(track.album)}</div><div class="pills">{score}{energy}{bpm}{extra_features}</div><div class="why">{escape(track.explanation)}</div><div class="source-note">Catalog: {escape(", ".join(sorted(track.sources)))}</div>'
    st.markdown(f'<div class="song-card">{image}<div>{details}</div></div>', unsafe_allow_html=True)
    cols = st.columns([1, 1, 3])
    if track.preview_url:
        with cols[0]:
            preview_format = "audio/mpeg" if track.preview_source in {"Deezer", "Spotify"} else "audio/mp4"
            st.audio(track.preview_url, format=preview_format)
    else:
        with cols[0]:
            st.caption("No official preview")
    if track.listen_url:
        with cols[1]:
            st.link_button("Listen ↗", track.listen_url, use_container_width=True, key=f"listen-{index}-{_clean(track.title)}")


def _discover(mood: str, country: str, limit: int, token: str | None) -> tuple[list[Track], list[str], bool]:
    rows: list[dict[str, Any]] = []
    errors: list[str] = []
    for term in MOOD_QUERIES[mood]:
        for label, lookup in (("Apple Music / iTunes", lambda t=term: search_itunes(t, country)), ("Deezer", lambda t=term: search_deezer(t))):
            try:
                rows.extend(lookup())
            except requests.RequestException:
                if label not in errors:
                    errors.append(label)
        if token:
            try:
                rows.extend(search_spotify(term, token))
            except requests.RequestException:
                if "Spotify" not in errors:
                    errors.append("Spotify")
    feature_access = False
    if token:
        spotify_ids = [row["track_id"] for row in rows if "Spotify" in row.get("sources", []) and row.get("track_id")]
        feature_map = spotify_features(spotify_ids, token)
        if feature_map:
            feature_access = True
            for row in rows:
                features = feature_map.get(row.get("track_id", "")) if "Spotify" in row.get("sources", []) else None
                if features:
                    row["features"].update(features)
    tracks = merge_tracks(rows)
    return rank_tracks(tracks, mood)[:limit], errors, feature_access


def main() -> None:
    _style()
    with st.sidebar:
        st.markdown('<div class="brand">mood<b>mix</b> ♫</div>', unsafe_allow_html=True)
        st.markdown("\n")
        st.markdown("### Set your mood")
        mood = st.selectbox("What are you feeling?", list(MOODS), label_visibility="collapsed")
        country = st.selectbox("Apple Music storefront", ["US", "CA", "GB", "AU", "IN"], index=0)
        count = st.slider("Songs to discover", min_value=6, max_value=18, value=12, step=3)
        st.markdown("---")
        st.markdown("**Optional · richer mood matching**")
        st.caption("Spotify audio features can improve ranking. This endpoint is deprecated and may be unavailable to your app.")
        client_id = st.text_input("Spotify client ID", value=os.getenv("SPOTIFY_CLIENT_ID", ""), type="password")
        client_secret = st.text_input("Spotify client secret", value=os.getenv("SPOTIFY_CLIENT_SECRET", ""), type="password")
        st.caption("Credentials stay in this local session. Set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET to avoid entering them each time.")

    st.markdown(f'<div class="hero"><div class="eyebrow">A soundtrack for right now</div><h1>Find your<br><span>feeling.</span></h1><p>Mood first. Genre second. Discover real songs that meet you where you are, with official previews when available.</p></div>', unsafe_allow_html=True)
    mood_info = MOODS[mood]
    st.markdown(f'<div class="section-label">{mood_info["emoji"]} &nbsp; {mood} mood &nbsp; · &nbsp; {mood_info["description"]}</div>', unsafe_allow_html=True)
    if st.button("Discover songs", type="primary", use_container_width=False):
        token = spotify_token(client_id, client_secret) if client_id and client_secret else None
        if client_id and client_secret and not token:
            st.info("Spotify sign-in was unavailable. Continuing with Apple Music/iTunes and Deezer.")
        with st.spinner(f"Finding songs for {mood.lower()}…"):
            tracks, errors, feature_access = _discover(mood, country, count, token)
        st.session_state["results"] = tracks
        st.session_state["result_mood"] = mood
        st.session_state["source_errors"] = errors
        st.session_state["feature_access"] = feature_access

    if "results" not in st.session_state:
        st.markdown("<div class='song-card'><div><div class='song-title'>Your next favorite is waiting.</div><div class='song-artist'>Choose a mood, then start exploring.</div><div class='why'>Recommendations come from live music catalogs. Nothing is made up or downloaded.</div></div></div>", unsafe_allow_html=True)
        return
    results = st.session_state["results"]
    errors = st.session_state.get("source_errors", [])
    if errors:
        st.warning(f"Some sources did not respond: {', '.join(errors)}. Showing available results.")
    if not st.session_state.get("feature_access"):
        st.info("Detailed energy, valence, danceability, acousticness, and instrumentalness need Spotify feature access. In this session, mood scores use provider-returned tempo where available; missing values are shown as unavailable.")
    if not results:
        st.warning("No catalog results came back for this mood. Try again in a moment or choose another mood.")
        return
    scored = sum(track.score is not None for track in results)
    result_mood = st.session_state.get("result_mood", mood)
    st.markdown(f"**{len(results)} {result_mood} tracks** · {scored} with a mood score · Results from live catalogs")
    left, right = st.columns(2)
    for index, track in enumerate(results):
        target_column = left if index % 2 == 0 else right
        with target_column:
            _render_track(track, index)


if __name__ == "__main__":
    main()
