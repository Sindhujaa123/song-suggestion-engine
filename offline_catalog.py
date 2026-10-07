"""Small, bundled MoodMix starter catalog. No network calls are made to build suggestions."""

MOODS = {
    "Happy": {"emoji": "☀️", "description": "Bright, buoyant songs for a lift."},
    "Sad": {"emoji": "🌧️", "description": "Gentle songs for sitting with a feeling."},
    "Calm": {"emoji": "🌿", "description": "Soft edges, slow breaths, quiet focus."},
    "Romantic": {"emoji": "💗", "description": "Warm melodies and close-to-the-heart songs."},
    "Energetic": {"emoji": "⚡", "description": "A pulse that keeps you moving."},
    "Focus": {"emoji": "🎧", "description": "Steady listening for deep work."},
    "Nostalgic": {"emoji": "📼", "description": "Familiar-feeling melodies with a little distance."},
    "Late Night": {"emoji": "🌙", "description": "Unhurried tracks for the hours after dark."},
    "Motivational": {"emoji": "🔥", "description": "Forward motion, one track at a time."},
    "Dreamy": {"emoji": "☁️", "description": "Floaty textures and a soft sense of wonder."},
}

# Curated titles and artists only. No audio features, artwork, previews, albums, or
# track URLs are stored here; the app must not infer or fabricate those fields.
SONGS = [
    {"title": "Lovely Day", "artist": "Bill Withers", "mood": "Happy", "score": 98, "why": "A warm, uplifting vocal and easygoing feel make this a sunny pick."},
    {"title": "Walking on Sunshine", "artist": "Katrina and the Waves", "mood": "Happy", "score": 96, "why": "An exuberant sing-along with an unmistakably cheerful mood."},
    {"title": "September", "artist": "Earth, Wind & Fire", "mood": "Happy", "score": 94, "why": "A celebratory classic with a bright, joyful character."},
    {"title": "The Night We Met", "artist": "Lord Huron", "mood": "Sad", "score": 98, "why": "A wistful, reflective song that leans into longing."},
    {"title": "Someone Like You", "artist": "Adele", "mood": "Sad", "score": 96, "why": "A spare heartbreak ballad centered on loss and reflection."},
    {"title": "Liability", "artist": "Lorde", "mood": "Sad", "score": 93, "why": "An intimate piano ballad with a vulnerable, inward feel."},
    {"title": "Weightless", "artist": "Marconi Union", "mood": "Calm", "score": 98, "why": "A slow ambient instrumental suited to a quiet reset."},
    {"title": "Holocene", "artist": "Bon Iver", "mood": "Calm", "score": 95, "why": "Gentle layers and a measured delivery make space to unwind."},
    {"title": "Nuvole Bianche", "artist": "Ludovico Einaudi", "mood": "Calm", "score": 93, "why": "A restrained piano piece with a spacious, reflective mood."},
    {"title": "At Last", "artist": "Etta James", "mood": "Romantic", "score": 98, "why": "A classic love song carried by a warm, expressive vocal."},
    {"title": "Best Part", "artist": "Daniel Caesar feat. H.E.R.", "mood": "Romantic", "score": 96, "why": "A tender duet built around closeness and affection."},
    {"title": "Lover", "artist": "Taylor Swift", "mood": "Romantic", "score": 94, "why": "A heartfelt, intimate song about lasting love."},
    {"title": "Don't Stop Me Now", "artist": "Queen", "mood": "Energetic", "score": 98, "why": "A fast-moving, high-spirited performance that keeps building."},
    {"title": "Titanium", "artist": "David Guetta feat. Sia", "mood": "Energetic", "score": 95, "why": "A big electronic production and powerful vocal bring momentum."},
    {"title": "Can't Hold Us", "artist": "Macklemore & Ryan Lewis feat. Ray Dalton", "mood": "Energetic", "score": 93, "why": "Driving percussion and an anthemic chorus create forward motion."},
    {"title": "Intro", "artist": "The xx", "mood": "Focus", "score": 97, "why": "A minimal instrumental arrangement leaves room for concentration."},
    {"title": "Experience", "artist": "Ludovico Einaudi", "mood": "Focus", "score": 95, "why": "A repeating piano-led instrumental can sit quietly alongside work."},
    {"title": "Time", "artist": "Hans Zimmer", "mood": "Focus", "score": 93, "why": "A gradual instrumental build offers atmosphere without lyrics."},
    {"title": "Dreams", "artist": "Fleetwood Mac", "mood": "Nostalgic", "score": 98, "why": "Its familiar sound and reflective lyrics have a timeless feel."},
    {"title": "Fast Car", "artist": "Tracy Chapman", "mood": "Nostalgic", "score": 96, "why": "A story-driven song that looks back while imagining a different future."},
    {"title": "Landslide", "artist": "Fleetwood Mac", "mood": "Nostalgic", "score": 94, "why": "A reflective song about change, memory, and growing older."},
    {"title": "Pink + White", "artist": "Frank Ocean", "mood": "Late Night", "score": 97, "why": "Soft, atmospheric production gives this a late-hours feel."},
    {"title": "After Dark", "artist": "Mr.Kitty", "mood": "Late Night", "score": 95, "why": "A shadowy synth-pop atmosphere fits a nighttime listen."},
    {"title": "Nights", "artist": "Frank Ocean", "mood": "Late Night", "score": 93, "why": "A spacious, introspective track for winding down after dark."},
    {"title": "Unstoppable", "artist": "Sia", "mood": "Motivational", "score": 98, "why": "A resilient message and soaring chorus make it an encouraging pick."},
    {"title": "Rise Up", "artist": "Andra Day", "mood": "Motivational", "score": 96, "why": "A song of perseverance that builds toward an uplifting vocal peak."},
    {"title": "The Climb", "artist": "Miley Cyrus", "mood": "Motivational", "score": 94, "why": "Its lyrics focus on persistence through a difficult journey."},
    {"title": "Space Song", "artist": "Beach House", "mood": "Dreamy", "score": 98, "why": "Hazy textures and a floating arrangement create a dreamlike mood."},
    {"title": "Myth", "artist": "Beach House", "mood": "Dreamy", "score": 96, "why": "Soft-focus vocals and layered sound feel immersive and weightless."},
    {"title": "Sweet Disposition", "artist": "The Temper Trap", "mood": "Dreamy", "score": 94, "why": "Expansive guitars and an airy vocal give it a glowing, open feel."},
]
