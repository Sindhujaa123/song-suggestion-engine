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

- `offline_catalog.py` contains the US English catalog. `indian_catalog.json` contains the current Telugu-only India picks; the Telugu mood lists are being curated incrementally.
- Verified track links, album artwork URLs, and available official previews are stored in `catalog_media.json`. They are bundled; the app makes no catalog API calls while users browse.
- The Telugu picks are a small incremental catalog; some moods currently have no Telugu songs while they are being reviewed.
- The displayed fit score is editorial, not an audio-feature calculation. Energy and BPM are not included and are never guessed.
- The app does not download or redistribute music.
