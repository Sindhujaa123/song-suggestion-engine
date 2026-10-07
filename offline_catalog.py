"""Bundled editorial recommendations. The app makes no music API calls at runtime."""

MOODS = {
    "Happy": {"emoji": "☀️", "description": "Bright, buoyant songs for a lift."},
    "Sad": {"emoji": "🌧️", "description": "Gentle songs for sitting with a feeling."},
    "Breakup": {"emoji": "💔", "description": "Songs for the end of a relationship and everything around it."},
    "Calm": {"emoji": "🌿", "description": "Soft edges, slow breaths, quiet focus."},
    "Romantic": {"emoji": "💗", "description": "Warm melodies and close-to-the-heart songs."},
    "Energetic": {"emoji": "⚡", "description": "A pulse that keeps you moving."},
    "Focus": {"emoji": "🎧", "description": "Steady listening for deep work."},
    "Nostalgic": {"emoji": "📼", "description": "Familiar-feeling melodies with a little distance."},
    "Late Night": {"emoji": "🌙", "description": "Unhurried tracks for the hours after dark."},
    "Motivational": {"emoji": "🔥", "description": "Forward motion, one track at a time."},
    "Dreamy": {"emoji": "☁️", "description": "Floaty textures and a soft sense of wonder."},
}

# Every title and artist is a hand-selected real-world track. Scores are editorial
# mood-fit ratings, not measured acoustic features. Links/artwork/previews are added
# to the bundled media index and are never fetched from a music API by the app.
MOOD_SONGS = {
    "Happy": [
        ("Lovely Day", "Bill Withers", "A warm vocal and easygoing feel make this a sunny pick."),
        ("Walking on Sunshine", "Katrina and the Waves", "An exuberant sing-along with an unmistakably cheerful mood."),
        ("September", "Earth, Wind & Fire", "A celebratory classic with a bright, joyful character."),
        ("Good as Hell", "Lizzo", "An affirming message and confident delivery give it a feel-good lift."),
        ("Happy", "Pharrell Williams", "A buoyant celebration built around a simple, joyful hook."),
        ("I Wanna Dance with Somebody", "Whitney Houston", "A joyful pop chorus made for singing along."),
        ("Here Comes the Sun", "The Beatles", "A hopeful song about brighter days arriving."),
        ("Can't Stop the Feeling!", "Justin Timberlake", "A playful, upbeat pop song with a sunny outlook."),
        ("Three Little Birds", "Bob Marley & The Wailers", "A reassuring message delivered with a relaxed, positive spirit."),
        ("Unwritten", "Natasha Bedingfield", "An optimistic reminder that the next chapter is still open."),
    ],
    "Sad": [
        ("The Night We Met", "Lord Huron", "A wistful, reflective song that leans into longing."),
        ("Someone Like You", "Adele", "A spare heartbreak ballad centered on loss and reflection."),
        ("Liability", "Lorde", "An intimate piano ballad with a vulnerable, inward feel."),
        ("Fix You", "Coldplay", "A tender song about comfort through a difficult time."),
        ("All I Want", "Kodaline", "A yearning ballad about love and loss."),
        ("Back to Black", "Amy Winehouse", "A soulful portrait of heartbreak and returning to old pain."),
        ("Nothing Compares 2 U", "Sinéad O'Connor", "A direct expression of grief and missing someone."),
        ("Hurt", "Johnny Cash", "A stark, reflective performance about regret and time."),
        ("Skinny Love", "Bon Iver", "An intimate song about a relationship coming apart."),
        ("when the party's over", "Billie Eilish", "A hushed, vulnerable song about a painful goodbye."),
    ],
    "Breakup": [
        ("Someone Like You", "Adele", "A goodbye ballad about accepting that a former love has moved on."),
        ("The Night We Met", "Lord Huron", "A longing song about wishing a relationship could be returned to its beginning."),
        ("Back to Black", "Amy Winehouse", "A soulful account of heartbreak and returning to old pain."),
        ("All I Want", "Kodaline", "A yearning breakup ballad about missing someone who is gone."),
        ("Nothing Compares 2 U", "Sinéad O'Connor", "A direct expression of loss after a relationship ends."),
        ("when the party's over", "Billie Eilish", "A quiet farewell to a relationship that has become painful."),
        ("Skinny Love", "Bon Iver", "A fragile song about a relationship running out of room to survive."),
        ("The Scientist", "Coldplay", "A regretful look at a relationship and the wish to start over."),
        ("Hurt", "Johnny Cash", "A stark reflection on regret, pain, and what remains."),
        ("Liability", "Lorde", "An intimate song about feeling difficult to love and being left alone."),
    ],
    "Calm": [
        ("Weightless", "Marconi Union", "A slow ambient instrumental suited to a quiet reset."),
        ("Holocene", "Bon Iver", "Gentle layers and a measured delivery make space to unwind."),
        ("Nuvole Bianche", "Ludovico Einaudi", "A restrained piano piece with a spacious, reflective mood."),
        ("Clair de Lune", "Claude Debussy", "A delicate piano classic with a soft, unhurried feel."),
        ("Bloom", "The Paper Kites", "A gentle acoustic song with a close, intimate atmosphere."),
        ("Pink Moon", "Nick Drake", "A quiet, understated song for a slower moment."),
        ("River Flows in You", "Yiruma", "A flowing piano melody with a peaceful character."),
        ("To Build a Home", "The Cinematic Orchestra", "A patient, spacious arrangement that invites reflection."),
        ("Near Light", "Ólafur Arnalds", "A soft instrumental blend of piano and strings."),
        ("A Walk", "Tycho", "A mellow instrumental with a smooth, unhurried flow."),
    ],
    "Romantic": [
        ("At Last", "Etta James", "A classic love song carried by a warm, expressive vocal."),
        ("Best Part", "Daniel Caesar feat. H.E.R.", "A tender duet built around closeness and affection."),
        ("Lover", "Taylor Swift", "A heartfelt, intimate song about lasting love."),
        ("Can't Help Falling in Love", "Elvis Presley", "A gentle declaration of devotion and falling in love."),
        ("Make You Feel My Love", "Adele", "A promise of care and steadfast affection."),
        ("All of Me", "John Legend", "A direct love song celebrating a partner as they are."),
        ("Your Song", "Elton John", "A personal, unshowy expression of affection."),
        ("La Vie en Rose", "Louis Armstrong", "A romantic standard about seeing the world through love."),
        ("Perfect", "Ed Sheeran", "A sentimental song about finding a lifelong partner."),
        ("I Will Always Love You", "Whitney Houston", "A powerful ballad about enduring love and letting go."),
    ],
    "Energetic": [
        ("Don't Stop Me Now", "Queen", "A high-spirited performance that keeps building."),
        ("Titanium", "David Guetta feat. Sia", "A big electronic production and powerful vocal bring momentum."),
        ("Can't Hold Us", "Macklemore & Ryan Lewis feat. Ray Dalton", "An anthemic chorus and driving percussion create forward motion."),
        ("Levels", "Avicii", "A bright electronic dance track with an instantly recognizable hook."),
        ("Run the World (Girls)", "Beyoncé", "A bold, percussive anthem with an assertive vocal."),
        ("Mr. Brightside", "The Killers", "A propulsive rock song with a full-throttle sing-along chorus."),
        ("Uptown Funk", "Mark Ronson feat. Bruno Mars", "A lively funk-pop groove built for movement."),
        ("Lose Yourself", "Eminem", "An urgent performance about seizing an opportunity."),
        ("Sandstorm", "Darude", "A fast, instrumental dance track with relentless momentum."),
        ("The Middle", "Jimmy Eat World", "An energetic rock chorus with an encouraging message."),
    ],
    "Focus": [
        ("Intro", "The xx", "A minimal instrumental arrangement leaves room for concentration."),
        ("Experience", "Ludovico Einaudi", "A piano-led instrumental can sit quietly alongside work."),
        ("Time", "Hans Zimmer", "A gradual instrumental build offers atmosphere without lyrics."),
        ("Your Hand in Mine", "Explosions in the Sky", "A lyric-free instrumental that builds patiently."),
        ("First Breath After Coma", "Explosions in the Sky", "An instrumental with a gradual, measured progression."),
        ("Says", "Nils Frahm", "A repeating instrumental pattern that slowly opens up."),
        ("Open Eye Signal", "Jon Hopkins", "A steady electronic instrumental for sustained attention."),
        ("A Walk", "Tycho", "An even instrumental flow with no vocal lyrics."),
        ("An Ending (Ascent)", "Brian Eno", "A spacious ambient instrumental for a quieter workspace."),
        ("We Move Lightly", "Dustin O'Halloran", "A restrained piano piece with a gentle, consistent feel."),
    ],
    "Nostalgic": [
        ("Dreams", "Fleetwood Mac", "A familiar sound and reflective lyrics give it a timeless feel."),
        ("Fast Car", "Tracy Chapman", "A story-led song that looks back while imagining another future."),
        ("Landslide", "Fleetwood Mac", "A reflective song about change, memory, and growing older."),
        ("The Scientist", "Coldplay", "A piano ballad about looking back and wishing to begin again."),
        ("Wonderwall", "Oasis", "A familiar sing-along with a wistful, hopeful edge."),
        ("Everybody Wants to Rule the World", "Tears for Fears", "A recognizable eighties sound with a reflective undercurrent."),
        ("Take on Me", "a-ha", "A vivid pop classic that carries a strong sense of its era."),
        ("Vienna", "Billy Joel", "A reflective song about time, growing up, and slowing down."),
        ("Time After Time", "Cyndi Lauper", "A familiar promise of being there for someone."),
        ("Iris", "Goo Goo Dolls", "An earnest alternative rock song closely tied to its era."),
    ],
    "Late Night": [
        ("Pink + White", "Frank Ocean", "Soft, atmospheric production gives this a late-hours feel."),
        ("After Dark", "Mr.Kitty", "A shadowy synth-pop atmosphere fits a nighttime listen."),
        ("Nights", "Frank Ocean", "A spacious, introspective track for winding down after dark."),
        ("Do I Wanna Know?", "Arctic Monkeys", "A slow-burning song with a nocturnal, brooding mood."),
        ("The Hills", "The Weeknd", "Dark production and an after-hours perspective define the track."),
        ("Street Lights", "Kanye West", "A sparse, reflective song with a lonely night-drive feel."),
        ("Wicked Game", "Chris Isaak", "A slow, atmospheric song about desire and uncertainty."),
        ("Moon Song", "Phoebe Bridgers", "A quiet, intimate song that suits a solitary late night."),
        ("Midnight City", "M83", "A glowing, nighttime synth sound with a cinematic sweep."),
        ("The Less I Know the Better", "Tame Impala", "A hazy, reflective groove for the end of the day."),
    ],
    "Motivational": [
        ("Unstoppable", "Sia", "A resilient message and soaring chorus make it an encouraging pick."),
        ("Rise Up", "Andra Day", "A song of perseverance that builds toward an uplifting vocal peak."),
        ("The Climb", "Miley Cyrus", "Its lyrics focus on persistence through a difficult journey."),
        ("Eye of the Tiger", "Survivor", "A determined anthem about facing a challenge."),
        ("Stronger", "Kanye West", "A forceful message about coming back with more resolve."),
        ("Fight Song", "Rachel Platten", "An affirming pop anthem about reclaiming confidence."),
        ("Hall of Fame", "The Script feat. will.i.am", "A direct message about effort and pursuing a goal."),
        ("Roar", "Katy Perry", "A bright empowerment anthem about finding your voice."),
        ("Brave", "Sara Bareilles", "An encouraging song about speaking up and being yourself."),
        ("Beautiful Day", "U2", "An optimistic rock song about finding possibility in the present."),
    ],
    "Dreamy": [
        ("Space Song", "Beach House", "Hazy textures and a floating arrangement create a dreamlike mood."),
        ("Myth", "Beach House", "Soft-focus vocals and layered sound feel immersive and weightless."),
        ("Sweet Disposition", "The Temper Trap", "Expansive guitars and an airy vocal give it a glowing feel."),
        ("Dreams", "The Cranberries", "Airy vocals and shimmering guitars create a wistful atmosphere."),
        ("Fade Into You", "Mazzy Star", "A soft, hazy performance with a floating, intimate quality."),
        ("Cherry-coloured Funk", "Cocteau Twins", "Layered vocals and shimmering production create an otherworldly feel."),
        ("Youth", "Daughter", "A spacious, delicate arrangement with a hazy emotional tone."),
        ("Apocalypse", "Cigarettes After Sex", "A slow, atmospheric sound with a soft-focus mood."),
        ("Sunsetz", "Cigarettes After Sex", "A gentle, atmospheric song with a drifting quality."),
        ("Sugar for the Pill", "Slowdive", "A wash of guitars and soft vocals creates a floating sound."),
    ],
}

SONGS = [
    {"title": title, "artist": artist, "mood": mood, "score": 98 - index * 2, "why": why}
    for mood, picks in MOOD_SONGS.items()
    for index, (title, artist, why) in enumerate(picks)
]

# Ensure every mood has ten verified listen targets with direct, bundled links.
# Some well-matched tracks intentionally appear in more than one mood collection.
_MEDIA_FILL_INS = {
    "Calm": [("The Night We Met", "Lord Huron")],
    "Focus": [
        ("Weightless", "Marconi Union"), ("Nuvole Bianche", "Ludovico Einaudi"),
        ("Clair de Lune", "Claude Debussy"), ("Pink Moon", "Nick Drake"),
        ("River Flows in You", "Yiruma"), ("To Build a Home", "The Cinematic Orchestra"),
        ("Near Light", "Ólafur Arnalds"),
    ],
    "Nostalgic": [
        ("Here Comes the Sun", "The Beatles"), ("September", "Earth, Wind & Fire"),
        ("Three Little Birds", "Bob Marley & The Wailers"),
    ],
    "Late Night": [
        ("The Night We Met", "Lord Huron"), ("Someone Like You", "Adele"),
        ("Liability", "Lorde"), ("Back to Black", "Amy Winehouse"),
        ("Nothing Compares 2 U", "Sinéad O'Connor"), ("Skinny Love", "Bon Iver"),
    ],
    "Motivational": [
        ("Don't Stop Me Now", "Queen"), ("Titanium", "David Guetta feat. Sia"),
        ("Can't Hold Us", "Macklemore & Ryan Lewis feat. Ray Dalton"), ("Levels", "Avicii"),
        ("Run the World (Girls)", "Beyoncé"), ("Lose Yourself", "Eminem"),
        ("The Middle", "Jimmy Eat World"), ("Uptown Funk", "Mark Ronson feat. Bruno Mars"),
    ],
    "Dreamy": [
        ("Weightless", "Marconi Union"), ("Nuvole Bianche", "Ludovico Einaudi"),
        ("Clair de Lune", "Claude Debussy"), ("Bloom", "The Paper Kites"),
        ("Pink Moon", "Nick Drake"), ("River Flows in You", "Yiruma"),
        ("To Build a Home", "The Cinematic Orchestra"), ("Near Light", "Ólafur Arnalds"),
        ("A Walk", "Tycho"), ("After Dark", "Mr.Kitty"),
    ],
}

_BASE_SONGS = SONGS
_BASE_BY_KEY = {(song["title"].casefold(), song["artist"].casefold()): song for song in _BASE_SONGS}
try:
    import json
    from pathlib import Path

    _media_path = Path(__file__).with_name("catalog_media.json")
    _media = json.loads(_media_path.read_text(encoding="utf-8")) if _media_path.exists() else {}
    _media_keys = set(_media)
except (OSError, ValueError):
    _media_keys = set()

_bundled_songs = []
for _mood in MOODS:
    _originals = [song for song in _BASE_SONGS if song["mood"] == _mood]
    _selected = [song for song in _originals if f"{song['title'].casefold()}|{song['artist'].casefold()}" in _media_keys]
    _seen = {(song["title"].casefold(), song["artist"].casefold()) for song in _selected}
    for _title, _artist in _MEDIA_FILL_INS.get(_mood, []):
        _key = (_title.casefold(), _artist.casefold())
        if _key not in _seen and f"{_key[0]}|{_key[1]}" in _media_keys and _key in _BASE_BY_KEY:
            _selected.append({**_BASE_BY_KEY[_key], "mood": _mood})
            _seen.add(_key)
    if _media_keys:
        _selected = _selected[:10]
    else:
        _selected = _originals[:10]
    for _index, _song in enumerate(_selected):
        _bundled_songs.append({**_song, "score": 98 - _index * 2})

SONGS = _bundled_songs
