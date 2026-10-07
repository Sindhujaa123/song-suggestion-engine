from urllib.parse import quote_plus

import streamlit as st

from offline_catalog import MOODS, SONGS


st.set_page_config(page_title="MoodMix · Find your feeling", page_icon="♫", layout="wide")


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
    .art-placeholder { width:106px; height:106px; flex:0 0 106px; display:grid; place-items:center; border-radius:12px; background:linear-gradient(145deg,#343047,#20202b 72%); color:#d5f36a; font-size:2rem; }
    .song-title { font:700 1rem Arial,sans-serif; color:#f4f2ed; margin:3px 0; }
    .song-artist { color:#b0aeb9; font-size:.86rem; }
    .pill-row { display:flex; flex-wrap:wrap; gap:6px; margin-top:10px; }
    .pill { border:1px solid rgba(255,255,255,.11); border-radius:99px; padding:4px 8px; color:#d0ced6; font-size:.69rem; }
    .pill-score { border-color:rgba(213,243,106,.28); background:rgba(213,243,106,.09); color:var(--lime); }
    .why { color:#a9a8b1; font-size:.76rem; margin-top:9px; line-height:1.45; }
    .stButton > button { border-radius:12px; }
    </style>""", unsafe_allow_html=True)


def render_song(song: dict[str, object], country: str, index: int) -> None:
    title = str(song["title"])
    artist = str(song["artist"])
    score = int(song["score"])
    why = str(song["why"])
    query = quote_plus(f"{title} {artist}")
    listen_url = f"https://music.apple.com/{country.lower()}/search?term={query}"
    st.markdown(
        f"""<div class="song-card">
        <div class="art-placeholder" aria-label="Album artwork unavailable in offline mode">♫</div>
        <div><div class="song-title">{title}</div><div class="song-artist">{artist}</div>
        <div class="pill-row"><span class="pill pill-score">{score}% curated mood fit</span>
        <span class="pill">Energy unavailable offline</span><span class="pill">BPM unavailable offline</span></div>
        <div class="why">{why}</div></div></div>""",
        unsafe_allow_html=True,
    )
    left, right = st.columns([1, 5])
    with left:
        st.link_button("Find to listen ↗", listen_url, use_container_width=True, key=f"listen-{index}-{query}")
    with right:
        st.caption("No preview is bundled. The button opens an Apple Music search for this title and artist.")


def main() -> None:
    add_styles()
    with st.sidebar:
        st.markdown('<div class="brand">mood<b>mix</b> ♫</div>', unsafe_allow_html=True)
        st.markdown("### Pick a mood")
        mood = st.selectbox("Mood", list(MOODS), label_visibility="collapsed")
        country = st.selectbox("Listening link region", ["US", "CA", "GB", "AU", "IN"], index=0)
        st.markdown("---")
        st.caption("Offline catalogue · no music APIs or credentials needed")

    info = MOODS[mood]
    st.markdown(
        f'<div class="hero"><div class="eyebrow">A soundtrack for right now</div><h1>Find your<br><span>feeling.</span></h1><p>Mood first. Genre second. Browse a small, bundled collection of real songs without waiting on music API services.</p></div>',
        unsafe_allow_html=True,
    )
    st.markdown(f'<div class="section-label">{info["emoji"]} &nbsp; {mood} mood &nbsp; · &nbsp; {info["description"]}</div>', unsafe_allow_html=True)
    songs = [song for song in SONGS if song["mood"] == mood]
    songs.sort(key=lambda song: int(song["score"]), reverse=True)
    st.info("Mood scores are editorial fits from the bundled catalogue. This offline version has no sourced energy/BPM data, artwork, or official previews, so those are marked unavailable.")
    st.markdown(f"**{len(songs)} curated picks** · bundled locally · no catalog requests")
    left, right = st.columns(2)
    for index, song in enumerate(songs):
        target = left if index % 2 == 0 else right
        with target:
            render_song(song, country, index)


if __name__ == "__main__":
    main()
