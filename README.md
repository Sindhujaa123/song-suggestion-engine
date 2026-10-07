# MoodMix

MoodMix is an offline-first Streamlit song-discovery app. Pick from Happy, Sad, Calm, Romantic, Energetic, Focus, Nostalgic, Late Night, Motivational, or Dreamy to browse bundled editorial recommendations. Runtime recommendations make no music-catalog API requests and need no provider credentials.

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

## Offline catalog limits

- Song titles, artists, mood notes, and editorial fit scores are bundled in `offline_catalog.py`.
- The fit score is a human-curated mood fit, not an audio-feature calculation.
- Energy, BPM, album artwork, and official previews are not bundled and are shown as unavailable. MoodMix does not estimate or invent them.
- “Find to listen” opens a search for that title and artist on Apple Music. The link is a search link, not a verified direct song URL.
- The app does not download or redistribute music.
