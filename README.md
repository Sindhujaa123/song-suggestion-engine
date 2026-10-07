# MoodMix

MoodMix is an offline-first Streamlit song-discovery app. Choose a US English or Indian catalog (Hindi and Telugu), then pick Happy, Sad, Breakup, Calm, Romantic, Energetic, Focus, Nostalgic, Late Night, Motivational, or Dreamy. Runtime recommendations make no music-catalog API requests and need no provider credentials.

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

- Each mood has ten curated song picks in both `offline_catalog.py` (US English) and `indian_catalog.json` (Hindi and Telugu).
- Verified track links, album artwork URLs, and available official previews are stored in `catalog_media.json`. They are bundled; the app makes no catalog API calls while users browse.
- Some songs intentionally appear in more than one mood collection so every category has ten verified listening links.
- The displayed fit score is editorial, not an audio-feature calculation. Energy and BPM are not included and are never guessed.
- The app does not download or redistribute music.
