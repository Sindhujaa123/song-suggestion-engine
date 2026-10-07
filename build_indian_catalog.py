"""Build the bundled Telugu catalog from manually curated, sourced picks."""
import json
from pathlib import Path
from urllib.parse import quote_plus


# Telugu-language editorial playlists/articles informed each collection; mood
# assignments and fit scores are MoodMix editorial curation.
PICKS = {
    "Happy": {
        "source": "https://music.amazon.in/playlists/B08DY5RWV4",
        "songs": [
            ("Butta Bomma", "Armaan Malik"), ("Ramuloo Ramulaa", "Anurag Kulkarni & Mangli"),
            ("Vachinde", "Madhu Priya & Ramky"), ("Seeti Maar", "Jaspreet Jasz & Rita"),
            ("Cinema Choopistha Mava", "Simha & Sravana Bhargavi"), ("Ringa Ringa", "Devi Sri Prasad"),
            ("Top Lesi Poddi", "Sagar & Geetha Madhuri"), ("Blockbuster", "Nakash Aziz & Shreya Ghoshal"),
            ("Swing Zara", "Hema Chandra & Jithin"), ("Dimaak Kharaab", "Keerthana Sharma & Saketh Komanduri"),
        ],
    },
    "Sad": {
        "source": "https://naahits.com/telugu-sad-songs-2026/",
        "songs": [
            ("Tharagathi Pathos", "Kaala Bhairava"), ("Kanulalo Thadigaa", "Chaitra Ambadipudi"),
            ("Telisiney Na Nuvvey", "Revanth"), ("Oosupodu", "Hemachandra"),
            ("Undiporaadhey (Sad Version)", "Sid Sriram"), ("Kanureppala Kaalam", "Gopi Sundar"),
            ("Adhento Gaani Vunnapaatuga", "Anirudh Ravichander & Sid Sriram"), ("Priyathama", "Sid Sriram"),
            ("Gaaju Bomma", "Hesham Abdul Wahab"), ("Nannaku Prematho (Title Song)", "Sagar"),
        ],
    },
    "Breakup": {
        "source": "https://www.youtube.com/watch?v=yvnsgYQyGXo",
        "songs": [
            ("Selavanuko", "Chaitra"), ("Em Cheppanu", "Karthik"), ("Povodhe Prema", "Yuvan Shankar Raja"),
            ("Atu Nuvve", "Neha Bhasin"), ("Manase Baruvai", "Kaarthi"), ("Yellipoke Shyamala", "Karthik"),
            ("Telisiney Na Nuvvey", "Revanth"), ("Oosupodu", "Hemachandra"),
            ("Undiporaadhey (Sad Version)", "Sid Sriram"), ("Cheppave Balamani", "Sweekar Agasthi"),
        ],
    },
    "Calm": {
        "source": "https://music.apple.com/us/playlist/telugu-chill/pl.f03fc63713b7451abb1a67a7e8e40a5e",
        "songs": [
            ("Paruvam Vanaga", "S. P. Balasubrahmanyam & Sujatha"), ("Ammaadi", "Shakthisree Gopalan & Kaala Bhairava"),
            ("Doorame Theeramai", "Harshavardhan Rameshwar & Sameera Bharadwaj"), ("Anuvanuvuu", "Arijit Singh"),
            ("O Cheli Thaara", "Haricharan"), ("Vintunnava", "Karthik"),
            ("Priyathama Priyathama", "Chinmayi Sripada"), ("Vellipomaakey", "Sid Sriram"),
            ("Yenti Yenti", "Chinmayi Sripada"), ("Nadhive", "Hesham Abdul Wahab & Rakendu Mouli"),
        ],
    },
    "Romantic": {
        "source": "https://music.apple.com/in/playlist/telugu-romance/pl.309ff6f19ad74c638af2d8d7caa3b464",
        "songs": [
            ("Chuttamalle", "Shilpa Rao"), ("Inkem Inkem Inkem Kaavaale", "Sid Sriram"),
            ("Samajavaragamana", "Sid Sriram"), ("Ninnila", "Armaan Malik"),
            ("Uppenantha", "KK"), ("Nenu Nuvvantu", "Naresh Iyer"), ("Emai Poyave", "Sid Sriram"),
            ("Kadalalle", "Sid Sriram & Aishwarya Ravichandran"), ("Adiga Adiga", "Sid Sriram"),
            ("Yentha Sakkagunnave", "Devi Sri Prasad"),
        ],
    },
    "Energetic": {
        "source": "https://music.amazon.in/playlists/B08DCKR395",
        "songs": [
            ("Race Gurram", "Usha Uthup & Thaman S"), ("Nee Dookudu", "Shankar Mahadevan"),
            ("Salam Rocky Bhai (Telugu)", "Vijay Prakash"), ("Fire Song (Telugu)", "Anurag Kulkarni & Deepthi Suresh"),
            ("Bhairava Anthem (Telugu)", "Diljit Dosanjh & Deepak Blue"), ("Top Lesi Poddi", "Sagar & Geetha Madhuri"),
            ("Ringa Ringa", "Devi Sri Prasad"), ("Ramuloo Ramulaa", "Anurag Kulkarni & Mangli"),
            ("Naatu Naatu", "Rahul Sipligunj & Kaala Bhairava"), ("Cinema Choopistha Mava", "Simha & Sravana Bhargavi"),
        ],
    },
    "Focus": {
        "source": "https://music.amazon.in/playlists/B0DKWXT84P",
        "songs": [
            ("Anuvanuvuu (Lofi Mix)", "Sunny M.R. & Arijit Singh"), ("Chandrakala (Lofi Mix)", "Hariharan & Rita Thyagarajan"),
            ("Ranguladdhukunna (Lofi Mix)", "Yazin Nizar & Haripriya"), ("Gundellonaa (Lofi Mix)", "Anirudh Ravichander"),
            ("Samajavaragamana (Lo-Fi Mix)", "Sid Sriram"), ("Kalaavathi (Lo-Fi Mix)", "Sid Sriram"),
            ("Rendu Kallu (Chill Lofi)", "Armaan Malik"), ("Urike Urike (Lo-Fi)", "Sid Sriram & Ramya Behara"),
            ("Emitemitemo (Lofi Mix)", "Alphonse"), ("Chamkeela Angeelesi (Lofi Mix)", "Ram Miriyala & Dhee"),
        ],
    },
    "Nostalgic": {
        "source": "https://music.amazon.in/playlists/B07DWXXXFK",
        "songs": [
            ("Nannu Vadali", "Ghantasala & P. Susheela"), ("Brindhavana Midhi", "A. M. Rajah & P. Susheela"),
            ("Naa Paata Nee Nota", "Ghantasala & P. Susheela"), ("Oho Meghamaala", "Ghantasala & P. Leela"),
            ("Nannu Dochu Kunduvatey", "P. Susheela & Ghantasala"), ("Pagale Vennela", "S. Janaki"),
            ("Chitapata Chinukulu", "S. P. Balasubrahmanyam & K. S. Chithra"), ("Telephone Dhwani La", "Hariharan & Harini"),
            ("Pachani Chilukalu", "K. J. Yesudas"), ("Lahiri Lahiri Lo", "Ghantasala & P. Susheela"),
        ],
    },
    "Late Night": {
        "source": "https://music.amazon.in/playlists/B07B89PW3Z",
        "songs": [
            ("Paruvam Vanaga", "S. P. Balasubrahmanyam & Sujatha"), ("Ammaadi", "Shakthisree Gopalan & Kaala Bhairava"),
            ("Doorame Theeramai", "Harshavardhan Rameshwar & Sameera Bharadwaj"), ("Anuvanuvuu", "Arijit Singh"),
            ("O Cheli Thaara", "Haricharan"), ("Yedo Yedo", "Karthik & Harini Ivaturi"),
            ("Priyathama Priyathama", "Chinmayi Sripada"), ("Vellipomaakey", "Sid Sriram"),
            ("Nadhive", "Hesham Abdul Wahab & Rakendu Mouli"), ("Emai Poyave", "Sid Sriram"),
        ],
    },
    "Motivational": {
        "source": "https://www.chaibisket.com/blogs/blog/highly-inspiring-songs-from-telugu-movies",
        "songs": [
            ("Tarali Raada", "S. P. Balasubrahmanyam"), ("Mounam Gane Edagamani", "S. P. Balasubrahmanyam"),
            ("Nee Prashnalu Neeve", "S. P. Balasubrahmanyam"), ("Chal Chalo Chalo", "Raghu Dixit, Sooraj Santhosh & Rita"),
            ("Spirit of Jersey", "Kaala Bhairava"), ("Ghal Ghal", "Udit Narayan & Chitra"),
            ("Oke Oka Jeevitham", "Javed Ali"), ("Jaago", "Ranjith"),
            ("Ekkutholimettu", "S. P. Balasubrahmanyam"), ("Marii Anthaga Maha Chintaga", "S. P. Balasubrahmanyam"),
        ],
    },
    "Dreamy": {
        "source": "https://naahits.com/telugu-love-songs/",
        "songs": [
            ("Chuttamalle", "Shilpa Rao"), ("Emai Poyave", "Sid Sriram"),
            ("Ninnila", "Armaan Malik"), ("Kadalalle", "Sid Sriram & Aishwarya Ravichandran"),
            ("Inkem Inkem Inkem Kaavaale", "Sid Sriram"), ("Aamani Paadave", "S. P. Balasubrahmanyam & S. Janaki"),
            ("O Cheli Thaara", "Haricharan"), ("Ninnukori Varnam", "S. P. Balasubrahmanyam & S. Janaki"),
            ("Vennelave Vennelave", "Hariharan & Sadhana Sargam"), ("Yamuna Teeram", "Hariharan & Chitra"),
        ],
    },
}

WHY = {
    "Happy": "An upbeat Telugu pick for its bright, buoyant feel and easy sing-along energy.",
    "Sad": "A Telugu emotional ballad selected for reflective melodies and a wistful tone.",
    "Breakup": "A Telugu heartbreak song chosen for lyrics and performance centered on separation or loss.",
    "Calm": "A softer Telugu melody selected for gentle pacing and a relaxed, soothing feel.",
    "Romantic": "A Telugu love song selected for its affectionate lyrics and warm melody.",
    "Energetic": "A high-energy Telugu track selected for its driving rhythm and movement-friendly pulse.",
    "Focus": "A mellow Telugu lo-fi version selected for unobtrusive, steady background listening.",
    "Nostalgic": "A Telugu classic selected for its timeless sound and strong throwback appeal.",
    "Late Night": "A subdued Telugu melody selected for unhurried listening after dark.",
    "Motivational": "A Telugu inspirational song selected for its forward-looking message and uplifting tone.",
    "Dreamy": "A flowing Telugu melody selected for its soft, romantic, floaty atmosphere.",
}


def main():
    output = []
    for mood, section in PICKS.items():
        for index, (title, artist) in enumerate(section["songs"]):
            output.append({
                "title": title,
                "artist": artist,
                "language": "Telugu",
                "market": "India",
                "mood": mood,
                "score": 98 - index * 2,
                "why": WHY[mood],
                "source_url": section["source"],
                "listen_url": "https://music.youtube.com/search?q=" + quote_plus(f"{title} {artist} Telugu"),
            })
    Path(__file__).with_name("indian_catalog.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
