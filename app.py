import streamlit as st

# --- Movie Database ---
# The comprehensive movie database with added entries for full language-genre coverage
movies_data = [
    # Hindi Movies
    {
        'title': 'Pathaan', 'language': 'hindi', 'genre': 'action',
        'description': 'An exiled RAW agent takes on a dangerous terrorist group led by a former agent with a vendetta. He must stop their deadly plan to unleash a biological weapon on India.',
        'director': 'Siddharth Anand', 'rating': '6.0/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Dangal', 'language': 'hindi', 'genre': 'action',
        'description': 'Based on the true story of Mahavir Singh Phogat, a former wrestler who trains his daughters Geeta and Babita to become world-class wrestlers. The film showcases their journey and struggles against societal norms.',
        'director': 'Nitesh Tiwari', 'rating': '8.3/10', 'platform': 'Netflix'
    },
    {
        'title': 'Dilwale Dulhania Le Jayenge', 'language': 'hindi', 'genre': 'comedy',
        'description': 'A young man and woman fall in love during a trip to Europe, but her strict father has already arranged her marriage. He follows her to India to win over her family without her father\'s knowledge.',
        'director': 'Aditya Chopra', 'rating': '8.0/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': '3 Idiots', 'language': 'hindi', 'genre': 'comedy',
        'description': 'Two friends embark on a quest to find their third companion, who disappeared after graduation, while reminiscing about their college days. The film satirizes the pressures of the Indian education system.',
        'director': 'Rajkumar Hirani', 'rating': '8.4/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Ra.One', 'language': 'hindi', 'genre': 'scifi',
        'description': 'A video game designer creates a virtual villain who escapes into the real world, forcing the designer\'s son to bring his superhero creation to life. The superhero must protect his family and the world from the rogue antagonist.',
        'director': 'Anubhav Sinha', 'rating': '4.7/10', 'platform': 'Netflix'
    },
    {
        'title': 'Krrish', 'language': 'hindi', 'genre': 'scifi',
        'description': 'Krishna, a young man with superpowers, falls in love and travels to Singapore, where he discovers his destiny as a superhero. He must use his abilities to fight evil and protect humanity.',
        'director': 'Rakesh Roshan', 'rating': '6.4/10', 'platform': 'Disney+ Hotstar'
    },
    {
        'title': 'Sholay', 'language': 'hindi', 'genre': 'action',
        'description': 'Two small-time crooks are hired by a retired police officer to capture a ruthless dacoit named Gabbar Singh. Their mission leads to a series of thrilling confrontations and emotional sacrifices.',
        'director': 'Ramesh Sippy', 'rating': '8.1/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Hera Pheri', 'language': 'hindi', 'genre': 'comedy',
        'description': 'Three unemployed men accidentally get involved in a kidnapping plot after a wrong number call. Their hilarious attempts to get rich lead to utter chaos and confusion.',
        'director': 'Priyadarshan', 'rating': '8.2/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'PK', 'language': 'hindi', 'genre': 'scifi',
        'description': 'An alien lands on Earth and loses his remote control, which is essential for his return home. He embarks on a quest to find it, questioning religious dogmas and human beliefs along the way.',
        'director': 'Rajkumar Hirani', 'rating': '8.1/10', 'platform': 'Netflix'
    },
    {
        'title': 'Stree', 'language': 'hindi', 'genre': 'horror',
        'description': 'In a town where a female spirit abducts men during a four-day festival, a tailor and his friends try to uncover the mystery. They must find a way to protect the town from the supernatural entity.',
        'director': 'Amar Kaushik', 'rating': '7.5/10', 'platform': 'Netflix'
    },
    {
        'title': 'Bhool Bhulaiyaa', 'language': 'hindi', 'genre': 'horror',
        'description': 'An American-educated psychiatrist is called to a family mansion when a newlywed couple experiences strange occurrences. He tries to solve the mystery of a vengeful spirit haunting the house.',
        'director': 'Priyadarshan', 'rating': '7.4/10', 'platform': 'Disney+ Hotstar'
    },
    # New Hindi Movie for Fantasy (placeholder)
    {
        'title': 'Brahmastra: Part One – Shiva', 'language': 'hindi', 'genre': 'fantasy',
        'description': 'A young man named Shiva discovers he has a mysterious connection with fire and is part of a secret society that protects powerful astras. He must learn to control his powers and stop a dark force threatening the world.',
        'director': 'Ayan Mukerji', 'rating': '5.6/10', 'platform': 'Disney+ Hotstar'
    },
    {
        'title': 'Tumbbad', 'language': 'hindi', 'genre': 'fantasy',
        'description': 'In a cursed village, a man becomes obsessed with finding a hidden treasure guarded by an ancient supernatural entity. His greed leads him deeper into a dark and mysterious world.',
        'director': 'Rahi Anil Barve', 'rating': '8.2/10', 'platform': 'Amazon Prime Video'
    },

    # Telugu Movies
    {
        'title': 'Baahubali: The Beginning', 'language': 'telugu', 'genre': 'action',
        'description': 'A young man discovers his royal lineage and destiny to reclaim his rightful place as king of Mahishmati. The film is a grand epic of war, betrayal, and heroism.',
        'director': 'S. S. Rajamouli', 'rating': '8.0/10', 'platform': 'Disney+ Hotstar'
    },
    {
        'title': 'Ala Vaikunthapurramuloo', 'language': 'telugu', 'genre': 'comedy',
        'description': 'Bantu, a young man who is often overlooked by his father, discovers he was swapped at birth and is actually the heir to a wealthy family. He then embarks on a journey to claim his true identity and place.',
        'director': 'Trivikram Srinivas', 'rating': '7.2/10', 'platform': 'Netflix'
    },
    {
        'title': 'Arjun Reddy', 'language': 'telugu', 'genre': 'action',
        'description': 'A brilliant but short-tempered surgeon spirals into self-destruction after his girlfriend is forced to marry another man. He struggles to cope with his heartbreak and addiction.',
        'director': 'Sandeep Reddy Vanga', 'rating': '8.1/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Pelli Choopulu', 'language': 'telugu', 'genre': 'comedy',
        'description': 'A modern take on arranged marriages, where a pragmatic aspiring chef and an ambitious but directionless young man meet for a traditional "pelli choopulu" (matchmaking session). They decide to start a food truck business together.',
        'director': 'Tharun Bhascker Dhaassyam', 'rating': '8.0/10', 'platform': 'Netflix'
    },
    {
        'title': 'Eega', 'language': 'telugu', 'genre': 'fantasy',
        'description': 'A murdered man is reincarnated as a housefly and seeks revenge on his killer. The fly uses its intelligence to torment and ultimately defeat the antagonist.',
        'director': 'S. S. Rajamouli', 'rating': '7.7/10', 'platform': 'Disney+ Hotstar'
    },
    {
        'title': 'Jersey', 'language': 'telugu', 'genre': 'action',
        'description': 'A talented but failed cricketer decides to return to the sport in his late thirties to fulfill his son\'s wish. He faces numerous challenges and skepticism on his journey.',
        'director': 'Gowtam Tinnanuri', 'rating': '8.5/10', 'platform': 'Netflix'
    },
    {
        'title': 'Agent Sai Srinivasa Athreya', 'language': 'telugu', 'genre': 'comedy',
        'description': 'A small-time detective from Nellore gets entangled in a high-profile case involving unidentified dead bodies. He uses his quirky methods to unravel the complex mystery.',
        'director': 'Swaroop RSJ', 'rating': '8.4/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Goodachari', 'language': 'telugu', 'genre': 'action',
        'description': 'An aspiring RAW agent gets framed for a murder and becomes a fugitive. He must clear his name and expose a larger conspiracy while on the run.',
        'director': 'Sashi Kiran Tikka', 'rating': '7.8/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Kshana Kshanam', 'language': 'telugu', 'genre': 'comedy',
        'description': 'A young woman witnesses a murder and is pursued by criminals, while a small-time thief gets involved in her escape. Their journey is filled with unexpected twists and humorous situations.',
        'director': 'Ram Gopal Varma', 'rating': '8.0/10', 'platform': 'Aha'
    },
    # New Telugu Movie for SciFi (placeholder)
    {
        'title': 'Cosmic Echoes', 'language': 'telugu', 'genre': 'scifi',
        'description': 'Scientists detect a mysterious signal from deep space that holds the key to humanity\'s future or its destruction. A team embarks on a perilous journey to uncover its origin.',
        'director': 'SciFi Telugu Director', 'rating': '7.1/10', 'platform': 'Zee5'
    },
    # New Telugu Movie for Horror (placeholder)
    {
        'title': 'The Haunted Mansion', 'language': 'telugu', 'genre': 'horror',
        'description': 'A family moves into an old, dilapidated mansion only to discover it is haunted by malevolent spirits. They must fight for their lives to escape the terrifying curse.',
        'director': 'Horror Telugu Director', 'rating': '6.9/10', 'platform': 'Sun NXT'
    },

    # Tamil Movies
    {
        'title': '24', 'language': 'tamil', 'genre': 'scifi',
        'description': 'A scientist invents a time-traveling watch, but his evil twin brother seeks to obtain it to alter his own past. The film follows the thrilling chase across different timelines.',
        'director': 'Vikram Kumar', 'rating': '7.9/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Enthiran', 'language': 'tamil', 'genre': 'scifi',
        'description': 'A brilliant scientist creates a humanoid robot named Chitti, who develops emotions and falls in love with his creator\'s fiancée. The robot then turns rogue, leading to a chaotic battle.',
        'director': 'S. Shankar', 'rating': '7.1/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Leo', 'language': 'tamil', 'genre': 'action',
        'description': 'A mild-mannered cafe owner is forced to reveal his violent past when a gang of criminals attacks his family. He must confront his hidden identity and protect his loved ones.',
        'director': 'Lokesh Kanagaraj', 'rating': '7.3/10', 'platform': 'Netflix'
    },
    {
        'title': 'Vikram Vedha', 'language': 'tamil', 'genre': 'action',
        'description': 'A tough police officer is on the hunt for a notorious gangster, but their encounter leads to a series of mind games and moral dilemmas. The film explores the blurred lines between good and evil.',
        'director': 'Pushkar-Gayathri', 'rating': '8.3/10', 'platform': 'Zee5'
    },
    {
        'title': 'Kaithi', 'language': 'tamil', 'genre': 'action',
        'description': 'An ex-convict on parole is caught in a night-long battle with drug lords while trying to meet his daughter for the first time. He must fight his way through a dangerous night to survive.',
        'director': 'Lokesh Kanagaraj', 'rating': '8.5/10', 'platform': 'Disney+ Hotstar'
    },
    {
        'title': 'Maanaadu', 'language': 'tamil', 'genre': 'scifi',
        'description': 'A man gets caught in a time loop and must prevent a political assassination to break free. He relives the same day repeatedly, trying to change the outcome.',
        'director': 'Venkat Prabhu', 'rating': '7.6/10', 'platform': 'SonyLIV'
    },
    {
        'title': 'Jigarthanda', 'language': 'tamil', 'genre': 'comedy',
        'description': 'An aspiring filmmaker tries to make a gangster film by secretly observing a real gangster, but his plans go awry. The film blends dark comedy with crime elements.',
        'director': 'Karthik Subbaraj', 'rating': '8.0/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Pizza', 'language': 'tamil', 'genre': 'horror',
        'description': 'A pizza delivery boy experiences supernatural events while delivering to a house, leading to a terrifying night. He struggles to distinguish reality from illusion.',
        'director': 'Karthik Subbaraj', 'rating': '7.6/10', 'platform': 'Disney+ Hotstar'
    },
    {
        'title': 'Maanagaram', 'language': 'tamil', 'genre': 'action',
        'description': 'The lives of several strangers intersect in a bustling city after a series of interconnected events. The film explores themes of fate and coincidence in an urban setting.',
        'director': 'Lokesh Kanagaraj', 'rating': '8.1/10', 'platform': 'Amazon Prime Video'
    },
    

    # Kannada Movies
    {
        'title': 'K.G.F: Chapter 1', 'language': 'kannada', 'genre': 'action',
        'description': 'A young man from the slums of Mumbai rises to become a powerful gangster, aiming to control the Kolar Gold Fields. He faces numerous challenges and enemies in his quest for power.',
        'director': 'Prashanth Neel', 'rating': '8.2/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Kirik Party', 'language': 'kannada', 'genre': 'comedy',
        'description': 'A group of engineering students navigate college life, friendships, and romance, experiencing both joy and heartbreak. The film captures the essence of youth and college nostalgia.',
        'director': 'Rishab Shetty', 'rating': '8.0/10', 'platform': 'Voot' # Changed director to match common knowledge for this film
    },
    {
        'title': 'Kantara', 'language': 'kannada', 'genre': 'action',
        'description': 'A fiery young man from a remote village finds himself in a conflict over land with the forest department, intertwined with local traditions and folklore. The film delves into the mystical practices and beliefs of the region.',
        'director': 'Rishab Shetty', 'rating': '8.3/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Ugramm', 'language': 'kannada', 'genre': 'action',
        'description': 'A man with a violent past tries to live a peaceful life, but circumstances force him to confront his old demons. He must protect his loved ones from dangerous adversaries.',
        'director': 'Prashanth Neel', 'rating': '8.0/10', 'platform': 'Sun NXT'
    },
    {
        'title': 'Love Mocktail', 'language': 'kannada', 'genre': 'comedy',
        'description': 'A man recounts his past relationships and heartbreaks to a young woman during a road trip. The film explores the complexities of love and growing up.',
        'director': 'Darling Krishna', 'rating': '8.3/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Rangitaranga', 'language': 'kannada', 'genre': 'horror',
        'description': 'A novelist returns to his ancestral village with his wife, where they encounter mysterious events and a local legend. They uncover dark secrets and a terrifying curse.',
        'director': 'Anup Bhandari', 'rating': '8.0/10', 'platform': 'Netflix'
    },
    {
        'title': 'Kavaludaari', 'language': 'kannada', 'genre': 'action',
        'description': 'A traffic police constable, bored with his routine job, takes up an old, unsolved case that leads him into a dangerous conspiracy. He must navigate a web of lies and corruption.',
        'director': 'Hemanth M. Rao', 'rating': '8.1/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Bell Bottom', 'language': 'kannada', 'genre': 'comedy',
        'description': 'A small-time detective in the 1980s gets his big break when he is hired to solve a series of unusual thefts. The film is a quirky and entertaining whodunit.',
        'director': 'Jayatheertha', 'rating': '8.0/10', 'platform': 'Sun NXT'
    },
    # New Kannada Movie for SciFi (placeholder)
    {
        'title': 'Lucia', 'language': 'kannada', 'genre': 'scifi',
        'description': 'A man suffering from insomnia begins taking an experimental pill that causes him to experience vivid dreams where his life is completely different. Soon, the line between his dream world and reality starts to blur.',
        'director': 'Pawan Kumar', 'rating': '8.3/10', 'platform': 'Amazon Prime Video'
    },

    {
        'title': 'Operation Alamelamma', 'language': 'kannada', 'genre': 'scifi',
        'description': 'A simple bank clerk suddenly finds himself entangled in a mysterious case involving advanced technology and a stolen device that could change the future. He must uncover the truth before it falls into the wrong hands.',
        'director': 'Suni', 'rating': '7.2/10', 'platform': 'Zee5'
    },
    # New Kannada Movie for Fantasy (placeholder)
    {
        'title': 'Vikrant Rona', 'language': 'kannada', 'genre': 'fantasy',
        'description': 'A mysterious police officer arrives in a haunted village where children have been disappearing under strange circumstances. As he investigates, supernatural forces and dark secrets begin to unfold.',
        'director': 'Anup Bhandari', 'rating': '7.0/10', 'platform': 'Disney+ Hotstar'
    },

    # English Movies
    {
        'title': 'The Matrix', 'language': 'english', 'genre': 'scifi',
        'description': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers. He must choose between blissful ignorance and and the harsh truth.',
        'director': 'The Wachowskis', 'rating': '8.7/10', 'platform': 'Hulu'
    },
    {
        'title': 'Inception', 'language': 'english', 'genre': 'scifi',
        'description': 'A thief who steals information by entering people\'s dreams is given the inverse task of planting an idea into a C.E.O.\'s subconscious. He assembles a team for this dangerous mission.',
        'director': 'Christopher Nolan', 'rating': '8.8/10', 'platform': 'Netflix'
    },
    {
        'title': 'Interstellar', 'language': 'english', 'genre': 'scifi',
        'description': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival. They embark on an epic journey beyond our galaxy.',
        'director': 'Christopher Nolan', 'rating': '8.7/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'Avengers: Endgame', 'language': 'english', 'genre': 'action',
        'description': 'Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the remaining Avengers must find a way to bring back their fallen allies.',
        'director': 'Anthony and Joe Russo', 'rating': '8.4/10', 'platform': 'Disney+ Hotstar'
    },
    {
        'title': 'Deadpool', 'language': 'english', 'genre': 'comedy',
        'description': 'A wisecracking mercenary with accelerated healing goes on a revenge spree against the man who gave him his powers. He breaks the fourth wall frequently, adding to the humor.',
        'director': 'Tim Miller', 'rating': '8.0/10', 'platform': 'Disney+ Hotstar'
    },
    {
        'title': 'The Conjuring', 'language': 'english', 'genre': 'horror',
        'description': 'Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse. They uncover a terrifying history linked to the property.',
        'director': 'James Wan', 'rating': '7.5/10', 'platform': 'Netflix'
    },
    {
        'title': 'Hereditary', 'language': 'english', 'genre': 'horror',
        'description': 'A grieving family is haunted by tragic and disturbing occurrences after the death of their secretive grandmother. They uncover sinister secrets about their ancestry.',
        'director': 'Ari Aster', 'rating': '7.3/10', 'platform': 'Amazon Prime Video'
    },
    {
        'title': 'The Lord of the Rings: The Fellowship of the Ring', 'language': 'english', 'genre': 'fantasy',
        'description': 'A young hobbit inherits a magical ring that holds the key to the destruction of Middle-earth. He embarks on a perilous quest with a fellowship of companions to destroy it.',
        'director': 'Peter Jackson', 'rating': '8.8/10', 'platform': 'HBO Max'
    },
    {
        'title': 'Harry Potter and the Sorcerer\'s Stone', 'language': 'english', 'genre': 'fantasy',
        'description': 'An orphaned boy discovers on his eleventh birthday that he is a wizard and is invited to study at Hogwarts School of Witchcraft and Wizardry. He soon uncovers a dark secret about his past.',
        'director': 'Chris Columbus', 'rating': '7.6/10', 'platform': 'Peacock'
    },
    {
        'title': 'The Invisible Man', 'language': 'english', 'genre': 'horror',
        'description': 'After her abusive ex-boyfriend commits suicide, a woman suspects she is being stalked by him, even though he is supposedly dead. She discovers he has found a way to become invisible.',
        'director': 'Leigh Whannell', 'rating': '7.1/10', 'platform': 'HBO Max'
    },
    {
        'title': 'Evil Dead Rise', 'language': 'english', 'genre': 'horror',
        'description': 'Two estranged sisters find their reunion cut short by the emergence of flesh-eating demons, thrusting them into a primal battle for survival. They must fight for their lives in a confined apartment building.',
        'director': 'Lee Cronin', 'rating': '6.5/10', 'platform': 'HBO Max'
    },
    {
        'title': 'Pan\'s Labyrinth', 'language': 'english', 'genre': 'fantasy',
        'description': 'In 1944 fascist Spain, a young girl escapes into a mystical world of fauns and fairies. She discovers she is a princess and must complete three dangerous tasks to gain immortality.',
        'director': 'Guillermo del Toro', 'rating': '8.2/10', 'platform': 'Netflix'
    },
    {
        'title': 'The Shape of Water', 'language': 'english', 'genre': 'fantasy',
        'description': 'At a top-secret research facility in the 1960s, a lonely janitor forms a unique relationship with an amphibious creature held in captivity. She plans to rescue him from his cruel captors.',
        'director': 'Guillermo del Toro', 'rating': '7.3/10', 'platform': 'Hulu'
    },
    {
        'title': 'Mad Max: Fury Road', 'language': 'english', 'genre': 'action',
        'description': 'In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler with the help of a drifter and a group of female prisoners. They embark on a high-octane chase across the desert.',
        'director': 'George Miller', 'rating': '8.1/10', 'platform': 'HBO Max'
    },
    {
        'title': 'The Grand Budapest Hotel', 'language': 'english', 'genre': 'comedy',
        'description': 'The adventures of a legendary concierge at a famous European hotel between the first and second World Wars, and his friendship with a young lobby boy. The film is known for its distinctive visual style and quirky humor.',
        'director': 'Wes Anderson', 'rating': '8.1/10', 'platform': 'HBO Max'
    },
    {
        'title': 'Arrival', 'language': 'english', 'genre': 'scifi',
        'description': 'When mysterious alien spacecrafts land across the globe, an elite team, led by linguist Louise Banks, is brought together to investigate. They race against time to communicate with the aliens before global war erupts.',
        'director': 'Denis Villeneuve', 'rating': '7.9/10', 'platform': 'Netflix'
    },
    {
        'title': 'Get Out', 'language': 'english', 'genre': 'horror',
        'description': 'A young African-American man visits his white girlfriend\'s parents for the first time, only to discover a sinister secret. He uncovers a disturbing truth about the family and their community.',
        'director': 'Jordan Peele', 'rating': '7.7/10', 'platform': 'Hulu'
    },
    {
        'title': 'Spirited Away', 'language': 'english', 'genre': 'fantasy',
        'description': 'During her family\'s move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts. She must find a way to save her parents and return home.',
        'director': 'Hayao Miyazaki', 'rating': '8.6/10', 'platform': 'HBO Max'
    },
]

if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

def toggle_theme():
    st.session_state.theme = 'light' if st.session_state.theme == 'dark' else 'dark'

# --- Streamlit UI Setup ---
st.set_page_config(layout="wide", page_title="CineSphere AI", page_icon="🎬")

# Dynamic CSS based on state
if st.session_state.theme == 'dark':
    bg_color = "#0e1117"
    card_color = "#1e2130"
    text_color = "#ffffff"
    sub_text = "#bdc3c7"
    bulb_icon = "💡"
    bulb_label = "Switch to Light Mode"
else:
    bg_color = "#f0f2f6"
    card_color = "#ffffff"
    text_color = "#1e2130"
    sub_text = "#555555"
    bulb_icon = "🕯️"
    bulb_label = "Switch to Dark Mode"

st.markdown(f"""
    <style>
    .stApp {{ background-color: {bg_color}; color: {text_color}; }}
    .movie-card {{
        background-color: {card_color};
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        border-left: 5px solid #e50914;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        color: {text_color};
    }}
    .rating-badge {{
        background-color: #f5c518;
        color: black;
        padding: 2px 8px;
        border-radius: 5px;
        font-weight: bold;
    }}
    h1, h2, h3, p {{ color: {text_color} !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Filters & Theme Toggle ---
with st.sidebar:
    st.title("⚙️ Controls")
    
    # Theme Toggle with Light Bulb Indicator
    st.write(f"### Theme: {st.session_state.theme.title()} {bulb_icon}")
    if st.button(bulb_label):
        toggle_theme()
        st.rerun()
    
    st.markdown("---")
    all_langs = sorted(list(set(m['language'] for m in movies_data)))
    all_gens = sorted(list(set(m['genre'] for m in movies_data)))
    
    sel_lang = st.selectbox("Language", [l.title() for l in all_langs])
    sel_gen = st.selectbox("Genre", [g.title() for g in all_gens])

# --- Main Content ---
st.title("🎬 CineSphere")
st.caption("Custom Movie Recommendations")
st.markdown("---")

filtered = [m for m in movies_data if m['language'] == sel_lang.lower() and m['genre'] == sel_gen.lower()]

if not filtered:
    st.error(f"No movies found for {sel_lang} {sel_gen}.")
else:
    cols = st.columns(2)
    for index, movie in enumerate(filtered):
        # Alternate between columns for a grid look
        with cols[index % 2]:
            st.markdown(f"""
            <div class="movie-card">
                <span class="rating-badge">⭐ {movie['rating']}</span>
                <h3 style="margin-top:10px;">{movie['title']}</h3>
                <p style="color:{sub_text}; font-style:italic;">Directed by {movie['director']}</p>
                <p>{movie['description']}</p>
                <small style="color:#007bff;">Stream on {movie['platform']}</small>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<center style='opacity: 0.5;'>Built with Streamlit • CinePal Engine</center>", unsafe_allow_html=True)
)
