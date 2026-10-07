# MoodMix

**MoodMix** is a Streamlit song discovery app built around how you feel, rather than music genres. Choose from Happy, Sad, Calm, Romantic, Energetic, Focus, Nostalgic, Late Night, Motivational, or Dreamy to discover catalog tracks with official artwork, preview snippets when provided, and links to listen.

## Run locally

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Apple Music/iTunes Search and Deezer results work without API credentials. To try richer audio-feature matching, optionally provide Spotify client credentials in the sidebar or as environment variables:

```powershell
$env:SPOTIFY_CLIENT_ID = "your-client-id"
$env:SPOTIFY_CLIENT_SECRET = "your-client-secret"
streamlit run app.py
```

Spotify's audio-features endpoint is deprecated and access can be denied. When that happens, MoodMix gracefully continues with real catalog data and any tempo values returned by its sources. It does not estimate missing audio features or invent tracks, preview URLs, or listening links. A match score is shown only when at least one real feature is available; the score compares returned features to the selected mood profile and renormalizes over features that exist for that track.

## Music sources

- [Apple iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/): song and artist metadata, artwork, official previews when supplied, and track links.
- [Deezer API](https://developers.deezer.com/api): search results with album artwork, preview URLs, listening links, and tempo when returned.
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/reference/get-audio-features): optional track search and real audio features (energy, valence, danceability, tempo, acousticness, instrumentalness), subject to Spotify access and deprecation limits.

Mood profiles are hand-set target values used for feature-distance ranking. Only provider-returned audio features affect a numeric match score. No full songs are downloaded or redistributed; previews are played from the official provider URL.
