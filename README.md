# MoodMix

MoodMix is an offline-first Streamlit song-discovery app. Choose the US English or Telugu catalog, then pick Happy, Sad, Breakup, Calm, Romantic, Energetic, Focus, Nostalgic, Late Night, Motivational, or Dreamy. Runtime recommendations make no music-catalog API requests and need no provider credentials.

## Run

With Python installed:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:STREAMLIT_CONFIG_DIR = (Join-Path (Get-Location) '.streamlit')
streamlit run app.py
```

If `pip` is not available as a command, use `uv`:

```powershell
uv venv --python 3.14 .venv
uv pip install --python .venv\Scripts\python.exe -r requirements.txt
$env:STREAMLIT_CONFIG_DIR = (Join-Path (Get-Location) '.streamlit')
.venv\Scripts\streamlit.exe run app.py
```

## Bundled catalog

- `offline_catalog.py` contains the US English catalog. `indian_catalog.json` contains 10 Telugu-language picks for each of the 11 moods.
- Verified track links, album artwork URLs, and available official previews are stored in `catalog_media.json`. They are bundled; the app makes no catalog API calls while users browse.
- Telugu picks also include a YouTube Music search link and a mood-level editorial source reference. These searches are clearly labeled and do not claim a song-specific official preview exists.
- The displayed fit score is editorial, not an audio-feature calculation. Energy and BPM are not included and are never guessed.
- The app does not download or redistribute music.

Telugu collection references include [Feel Good Tollywood](https://music.amazon.in/playlists/B08DY5RWV4), [Telugu Sad Songs](https://naahits.com/telugu-sad-songs-2026/), [Aditya Music's Telugu heartbreak collection](https://www.youtube.com/watch?v=yvnsgYQyGXo), [Telugu Chill](https://music.apple.com/us/playlist/telugu-chill/pl.f03fc63713b7451abb1a67a7e8e40a5e), [Telugu Romance](https://music.apple.com/in/playlist/telugu-romance/pl.309ff6f19ad74c638af2d8d7caa3b464), [Telugu Workout](https://music.amazon.in/playlists/B08DCKR395), [Lo-Fi Telugu](https://music.amazon.in/playlists/B0DKWXT84P), [60s Telugu Flashback](https://music.amazon.in/playlists/B07DWXXXFK), and [Telugu motivational songs](https://www.chaibisket.com/blogs/blog/highly-inspiring-songs-from-telugu-movies). The app mood-fit labels are editorial; the linked collections informed track and mood selection.
