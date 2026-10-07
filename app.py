import json
from pathlib import Path
from html import escape

import streamlit as st

from offline_catalog import MOODS, SONGS


st.set_page_config(page_title="MoodMix · Find your feeling", page_icon="♫", layout="wide")
MEDIA_FILE = Path(__file__).with_name("catalog_media.json")
INDIA_FILE = Path(__file__).with_name("indian_catalog.json")


def bundled_media() -> dict[str, dict[str, str]]:
    if not MEDIA_FILE.exists():
        return {}
    try:
        return json.loads(MEDIA_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def indian_songs() -> list[dict[str, object]]:
    if not INDIA_FILE.exists():
        return []
    try:
        data = json.loads(INDIA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        return []


def add_styles() -> None:
    st.markdown("""<style>
    :root { --ink:#f4f2ed; --muted:#aaa9b5; --line:rgba(255,255,255,.09); --lime:#d5f36a; }
    html, body, [class*="css"] { font-family:Arial,sans-serif; }
    .stApp { background:radial-gradient(ellipse at 74% -8%,rgba(126,91,190,.22),transparent 38%),#0d0d12; color:var(--ink); }
    .block-container { max-width:1240px; padding-top:1.35rem; }
    [data-testid="stSidebar"] { background:#111117; border-right:1px solid var(--line); }
    .brand { font:800 1.35rem Arial,sans-serif; letter-spacing:-.06em; color:#f7f5f0; }
    .brand b { color:var(--lime); }
    .hero { padding:2.7rem 0 1.2rem; }
    .hero .eyebrow { color:#c9d991; font-size:.72rem; font-weight:700; letter-spacing:.16em; text-transform:uppercase; }
    .hero h1 { font:800 clamp(2.7rem,6vw,5.1rem)/.98 Arial,sans-serif; letter-spacing:-.075em; margin:.7rem 0 1rem; }
    .hero h1 span { color:var(--lime); }
    .hero p { max-width:620px; color:#b1afba; font-size:1.02rem; line-height:1.65; }
    .section-label { color:#aaa9b5; font-size:.75rem; font-weight:700; letter-spacing:.13em; text-transform:uppercase; margin:.35rem 0 .85rem; }
    .song-card { display:flex; gap:15px; padding:14px; min-height:164px; border:1px solid var(--line); border-radius:18px; background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.018)); margin:0 0 12px; }
    .art-placeholder { width:106px; height:106px; flex:0 0 106px; display:grid; place-items:center; border-radius:12px; background:linear-gradient(145deg,#343047,#20202b 72%); color:#d5f36a; font-size:2rem; object-fit:cover; }
    .song-title { font:700 1rem Arial,sans-serif; color:#f4f2ed; margin:3px 0; }
    .song-artist { color:#b0aeb9; font-size:.86rem; }
    .pill-row { display:flex; flex-wrap:wrap; gap:6px; margin-top:10px; }
    .pill { border:1px solid rgba(255,255,255,.11); border-radius:99px; padding:4px 8px; color:#d0ced6; font-size:.69rem; }
    .pill-score { border-color:rgba(213,243,106,.28); background:rgba(213,243,106,.09); color:var(--lime); }
    .why { color:#a9a8b1; font-size:.76rem; margin-top:9px; line-height:1.45; }
    .stButton > button { border-radius:12px; }
    </style>""", unsafe_allow_html=True)


def render_song(song: dict[str, object], index: int, media_index: dict[str, dict[str, str]]) -> None:
    title = str(song["title"])
    artist = str(song["artist"])
    score = int(song["score"])
    why = str(song["why"])
    safe_title, safe_artist, safe_why = escape(title), escape(artist), escape(why)
    language = f' · {escape(str(song["language"]))}' if song.get("language") else ""
    media = media_index.get(f"{title.casefold()}|{artist.casefold()}", {})
    listen_url = media.get("listen_url") or str(song.get("listen_url", ""))
    source_url = str(song.get("source_url", ""))
    artwork = media.get("artwork_url")
    cover = f'<img class="art-placeholder" src="{escape(artwork, quote=True)}" alt="Album artwork">' if artwork else '<div class="art-placeholder" aria-label="Album artwork unavailable">♫</div>'
    st.markdown(
        f"""<div class="song-card">
        {cover}
        <div><div class="song-title">{safe_title}</div><div class="song-artist">{safe_artist}{language}</div>
        <div class="pill-row"><span class="pill pill-score">{score}% curated mood fit</span>
        <span class="pill">Energy unavailable offline</span><span class="pill">BPM unavailable offline</span></div>
        <div class="why">{safe_why}</div></div></div>""",
        unsafe_allow_html=True,
    )
    left, right = st.columns([1, 5])
    if listen_url:
        with left:
            st.link_button("Find on YouTube Music" if song.get("language") == "Telugu" else "Listen ↗", listen_url, use_container_width=True, key=f"listen-{index}-{title.casefold()}")
    if source_url and song.get("language") == "Telugu":
        with right:
            st.link_button("Curation source", source_url, key=f"source-{index}-{title.casefold()}")
    if media.get("preview_url"):
        with right:
            st.audio(media["preview_url"], format="audio/mp4")


def main() -> None:
    add_styles()
    with st.sidebar:
        st.markdown('<div class="brand">mood<b>mix</b> ♫</div>', unsafe_allow_html=True)
        market = st.radio("Choose music catalog", ["US · English", "India · Telugu"], label_visibility="visible")
        st.markdown("### Pick a mood")
        mood = st.selectbox("Mood", list(MOODS), label_visibility="collapsed")
        st.markdown("---")
        st.caption("Offline catalogue · no music APIs or credentials needed")

    info = MOODS[mood]
    media_index = bundled_media()
    st.markdown(
        f'<div class="hero"><div class="eyebrow">A soundtrack for right now</div><h1>Find your<br><span>feeling.</span></h1><p>Mood first. Genre second. Browse a small, bundled collection of real songs without waiting on music API services.</p></div>',
        unsafe_allow_html=True,
    )
    st.markdown(f'<div class="section-label">{info["emoji"]} &nbsp; {mood} mood &nbsp; · &nbsp; {info["description"]}</div>', unsafe_allow_html=True)
    if market.startswith("India"):
        songs = [song for song in indian_songs() if song["mood"] == mood and song.get("language") == "Telugu"]
    else:
        songs = [song for song in SONGS if song["mood"] == mood]
    songs.sort(key=lambda song: int(song["score"]), reverse=True)
    st.info("Mood scores are editorial fits, not audio-feature calculations. Telugu picks include a YouTube Music search link and a source used for curation. Official previews, artwork, energy, and BPM appear only when bundled data is available.")
    st.markdown(f"**{len(songs)} curated picks** · {market} · bundled locally · no catalog requests")
    left, right = st.columns(2)
    for index, song in enumerate(songs):
        target = left if index % 2 == 0 else right
        with target:
            render_song(song, index, media_index)


if __name__ == "__main__":
    main()
