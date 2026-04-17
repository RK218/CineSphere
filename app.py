import streamlit as st
movies_data = [
    # Hindi Movies
    {'title': 'Pathaan', 'language': 'hindi', 'genre': 'action', 'description': 'An exiled RAW agent takes on a dangerous terrorist group.', 'director': 'Siddharth Anand', 'rating': '6.0/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Dangal', 'language': 'hindi', 'genre': 'action', 'description': 'Mahavir Singh Phogat trains his daughters to become world-class wrestlers.', 'director': 'Nitesh Tiwari', 'rating': '8.3/10', 'platform': 'Netflix'},
    {'title': 'Sholay', 'language': 'hindi', 'genre': 'action', 'description': 'Two crooks are hired to capture a ruthless dacoit.', 'director': 'Ramesh Sippy', 'rating': '8.1/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Vikram Vedha', 'language': 'hindi', 'genre': 'action', 'description': 'A tough cop tracks a gangster who tells him stories that change his perspective.', 'director': 'Pushkar-Gayathri', 'rating': '7.1/10', 'platform': 'Voot'},
    {'title': 'Jawan', 'language': 'hindi', 'genre': 'action', 'description': 'A man is driven by a personal vendetta to rectify the wrongs in society.', 'director': 'Atlee', 'rating': '7.0/10', 'platform': 'Netflix'},

    {'title': '3 Idiots', 'language': 'hindi', 'genre': 'comedy', 'description': 'Two friends search for their long-lost companion while reminiscing about college.', 'director': 'Rajkumar Hirani', 'rating': '8.4/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Hera Pheri', 'language': 'hindi', 'genre': 'comedy', 'description': 'Three unemployed men get involved in a kidnapping plot.', 'director': 'Priyadarshan', 'rating': '8.2/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Andhadhun', 'language': 'hindi', 'genre': 'comedy', 'description': 'A blind pianist unknowingly becomes embroiled in a murder.', 'director': 'Sriram Raghavan', 'rating': '8.2/10', 'platform': 'Netflix'},
    {'title': 'Chupke Chupke', 'language': 'hindi', 'genre': 'comedy', 'description': 'A newlywed professor plays a prank on his wife\'s family.', 'director': 'Hrishikesh Mukherjee', 'rating': '8.3/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Stree', 'language': 'hindi', 'genre': 'comedy', 'description': 'Men live in fear of a spirit that abducts them at night.', 'director': 'Amar Kaushik', 'rating': '7.5/10', 'platform': 'Netflix'},

    {'title': 'PK', 'language': 'hindi', 'genre': 'scifi', 'description': 'An alien on Earth questions religious dogmas.', 'director': 'Rajkumar Hirani', 'rating': '8.1/10', 'platform': 'Netflix'},
    {'title': 'Ra.One', 'language': 'hindi', 'genre': 'scifi', 'description': 'A virtual villain enters the real world.', 'director': 'Anubhav Sinha', 'rating': '4.7/10', 'platform': 'Netflix'},
    {'title': 'Krrish', 'language': 'hindi', 'genre': 'scifi', 'description': 'Krishna uses his superpowers to fight evil.', 'director': 'Rakesh Roshan', 'rating': '6.4/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Mr. India', 'language': 'hindi', 'genre': 'scifi', 'description': 'A man discovers a watch that makes him invisible.', 'director': 'Shekhar Kapur', 'rating': '7.7/10', 'platform': 'Zee5'},
    {'title': 'Koi... Mil Gaya', 'language': 'hindi', 'genre': 'scifi', 'description': 'A mentally challenged youth befriends an alien.', 'director': 'Rakesh Roshan', 'rating': '7.1/10', 'platform': 'Zee5'},

    {'title': 'Tumbbad', 'language': 'hindi', 'genre': 'horror', 'description': 'A man searches for a hidden treasure in a cursed village.', 'director': 'Rahi Anil Barve', 'rating': '8.2/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Bhool Bhulaiyaa', 'language': 'hindi', 'genre': 'horror', 'description': 'A psychiatrist solves the mystery of a spirit in a mansion.', 'director': 'Priyadarshan', 'rating': '7.4/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Raat', 'language': 'hindi', 'genre': 'horror', 'description': 'A family experiences supernatural events in their new home.', 'director': 'Ram Gopal Varma', 'rating': '7.1/10', 'platform': 'Amazon Prime Video'},
    {'title': '13B: Fear Has a New Address', 'language': 'hindi', 'genre': 'horror', 'description': 'A man realizes a TV show is predicting his family\'s future.', 'director': 'Vikram Kumar', 'rating': '7.3/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Pari', 'language': 'hindi', 'genre': 'horror', 'description': 'A man helps a mysterious woman chained in a hut.', 'director': 'Prosit Roy', 'rating': '6.6/10', 'platform': 'Amazon Prime Video'},

    {'title': 'Brahmastra', 'language': 'hindi', 'genre': 'fantasy', 'description': 'Shiva discovers his connection to fire and ancient weapons.', 'director': 'Ayan Mukerji', 'rating': '5.6/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Paheli', 'language': 'hindi', 'genre': 'fantasy', 'description': 'A ghost falls in love with a newlywed woman.', 'director': 'Amol Palekar', 'rating': '6.4/10', 'platform': 'Netflix'},
    {'title': 'Bulbbul', 'language': 'hindi', 'genre': 'fantasy', 'description': 'A child bride grows up to be a mysterious woman in a village.', 'director': 'Anvita Dutt', 'rating': '6.6/10', 'platform': 'Netflix'},
    {'title': 'Makdee', 'language': 'hindi', 'genre': 'fantasy', 'description': 'A girl enters a haunted mansion to save her sister.', 'director': 'Vishal Bhardwaj', 'rating': '7.4/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Jaani Dushman', 'language': 'hindi', 'genre': 'fantasy', 'description': 'A shape-shifting snake seeks revenge for his lover.', 'director': 'Rajkumar Kohli', 'rating': '2.8/10', 'platform': 'YouTube'},

    # Telugu Movies
    {'title': 'Baahubali', 'language': 'telugu', 'genre': 'action', 'description': 'A prince learns about his heritage and fights for the throne.', 'director': 'S. S. Rajamouli', 'rating': '8.0/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'RRR', 'language': 'telugu', 'genre': 'action', 'description': 'Two revolutionaries fight against the British Raj.', 'director': 'S. S. Rajamouli', 'rating': '7.8/10', 'platform': 'Netflix'},
    {'title': 'Pushpa: The Rise', 'language': 'telugu', 'genre': 'action', 'description': 'A laborer rises in the world of red sandalwood smuggling.', 'director': 'Sukumar', 'rating': '7.6/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Arjun Reddy', 'language': 'telugu', 'genre': 'action', 'description': 'A surgeon spirals into self-destruction after heartbreak.', 'director': 'Sandeep Vanga', 'rating': '8.1/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Salaar', 'language': 'telugu', 'genre': 'action', 'description': 'A gang leader makes a promise to a dying friend.', 'director': 'Prashanth Neel', 'rating': '6.5/10', 'platform': 'Netflix'},

    {'title': 'Pelli Choopulu', 'language': 'telugu', 'genre': 'comedy', 'description': 'Two people meet for a matchmaking session and start a business.', 'director': 'Tharun Bhascker', 'rating': '8.0/10', 'platform': 'Netflix'},
    {'title': 'Mathu Vadalara', 'language': 'telugu', 'genre': 'comedy', 'description': 'A delivery boy gets stuck in a crime scene.', 'director': 'Ritesh Rana', 'rating': '8.2/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Jathi Ratnalu', 'language': 'telugu', 'genre': 'comedy', 'description': 'Three happy-go-lucky men end up in jail.', 'director': 'Anudeep KV', 'rating': '7.3/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Agent Sai Srinivasa Athreya', 'language': 'telugu', 'genre': 'comedy', 'description': 'A quirky detective solves a high-profile case.', 'director': 'Swaroop RSJ', 'rating': '8.4/10', 'platform': 'Amazon Prime Video'},
    {'title': 'F2: Fun and Frustration', 'language': 'telugu', 'genre': 'comedy', 'description': 'Two men try to control their wives and escape the madness.', 'director': 'Anil Ravipudi', 'rating': '6.2/10', 'platform': 'Amazon Prime Video'},

    {'title': 'Aditya 369', 'language': 'telugu', 'genre': 'scifi', 'description': 'People travel through time in a machine.', 'director': 'Singeetam Srinivasa Rao', 'rating': '8.2/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Oke Oka Jeevitham', 'language': 'telugu', 'genre': 'scifi', 'description': 'A musician travels back in time to save his mother.', 'director': 'Shree Karthick', 'rating': '7.9/10', 'platform': 'SonyLIV'},
    {'title': 'Ismart Shankar', 'language': 'telugu', 'genre': 'scifi', 'description': 'A memory chip is implanted in a contract killer.', 'director': 'Puri Jagannadh', 'rating': '5.5/10', 'platform': 'Zee5'},
    {'title': '7th Sense', 'language': 'telugu', 'genre': 'scifi', 'description': 'A genetic engineering student tries to revive Bodhidharma.', 'director': 'A.R. Murugadoss', 'rating': '6.2/10', 'platform': 'Zee5'},
    {'title': 'Kalki 2898 AD', 'language': 'telugu', 'genre': 'scifi', 'description': 'A modern avatar of Vishnu descends to protect the world.', 'director': 'Nag Ashwin', 'rating': '7.6/10', 'platform': 'Netflix'},

    {'title': 'Arundhati', 'language': 'telugu', 'genre': 'horror', 'description': 'A brave woman fights an evil sorcerer.', 'director': 'Kodi Ramakrishna', 'rating': '7.3/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Virupaksha', 'language': 'telugu', 'genre': 'horror', 'description': 'Mysterious deaths occur in a village due to a curse.', 'director': 'Karthik Varma', 'rating': '7.2/10', 'platform': 'Netflix'},
    {'title': 'Masooda', 'language': 'telugu', 'genre': 'horror', 'description': 'A man helps his neighbor when her daughter is possessed.', 'director': 'Sai Kiran', 'rating': '7.2/10', 'platform': 'Amazon Prime Video'},
    {'title': 'U-Turn', 'language': 'telugu', 'genre': 'horror', 'description': 'An intern investigates deaths at a flyover.', 'director': 'Pawan Kumar', 'rating': '7.0/10', 'platform': 'Netflix'},
    {'title': 'Bhaagamathie', 'language': 'telugu', 'genre': 'horror', 'description': 'An IAS officer is imprisoned in a haunted house.', 'director': 'G. Ashok', 'rating': '7.0/10', 'platform': 'Amazon Prime Video'},

    {'title': 'Eega', 'language': 'telugu', 'genre': 'fantasy', 'description': 'A man is reborn as a fly to take revenge.', 'director': 'S. S. Rajamouli', 'rating': '7.7/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Magadheera', 'language': 'telugu', 'genre': 'fantasy', 'description': 'A warrior reborn in the modern era seeks his love.', 'director': 'S. S. Rajamouli', 'rating': '7.7/10', 'platform': 'Aha'},
    {'title': 'Jagadeka Veerudu Athiloka Sundari', 'language': 'telugu', 'genre': 'fantasy', 'description': 'A man finds a ring belonging to a celestial being.', 'director': 'K. Raghavendra Rao', 'rating': '8.1/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Yamadonga', 'language': 'telugu', 'genre': 'fantasy', 'description': 'A thief ends up in Yamaloka and challenges the God of Death.', 'director': 'S. S. Rajamouli', 'rating': '7.3/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Karthikeya 2', 'language': 'telugu', 'genre': 'fantasy', 'description': 'A doctor searches for Lord Krishna\'s anklet.', 'director': 'Chandoo Mondeti', 'rating': '7.1/10', 'platform': 'Zee5'},

    # Tamil Movies
    {'title': 'Kaithi', 'language': 'tamil', 'genre': 'action', 'description': 'An ex-convict fights drug lords to reach his daughter.', 'director': 'Lokesh Kanagaraj', 'rating': '8.5/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Vikram', 'language': 'tamil', 'genre': 'action', 'description': 'A special ops team hunts for a mysterious killer.', 'director': 'Lokesh Kanagaraj', 'rating': '8.3/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Thuppakki', 'language': 'tamil', 'genre': 'action', 'description': 'An army officer hunts sleeper cells in Mumbai.', 'director': 'A.R. Murugadoss', 'rating': '8.1/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Leo', 'language': 'tamil', 'genre': 'action', 'description': 'A cafe owner confronts his violent past.', 'director': 'Lokesh Kanagaraj', 'rating': '7.3/10', 'platform': 'Netflix'},
    {'title': 'Vada Chennai', 'language': 'tamil', 'genre': 'action', 'description': 'A carrom player enters the world of crime.', 'director': 'Vetrimaaran', 'rating': '8.4/10', 'platform': 'Disney+ Hotstar'},

    {'title': 'Jigarthanda', 'language': 'tamil', 'genre': 'comedy', 'description': 'A filmmaker observes a gangster to make a movie.', 'director': 'Karthik Subbaraj', 'rating': '8.1/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Doctor', 'language': 'tamil', 'genre': 'comedy', 'description': 'A military doctor hunts human traffickers with a quirky family.', 'director': 'Nelson Dilipkumar', 'rating': '7.4/10', 'platform': 'Netflix'},
    {'title': 'Soodhu Kavvum', 'language': 'tamil', 'genre': 'comedy', 'description': 'Four kidnappers fail hilariously in their missions.', 'director': 'Nalan Kumarasamy', 'rating': '8.3/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Panchatanthiram', 'language': 'tamil', 'genre': 'comedy', 'description': 'Five friends get into trouble while on a trip.', 'director': 'K. S. Ravikumar', 'rating': '8.3/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Kadhalum Kadandhu Pogum', 'language': 'tamil', 'genre': 'comedy', 'description': 'An unlikely bond between a thug and an IT professional.', 'director': 'Nalan Kumarasamy', 'rating': '7.3/10', 'platform': 'Amazon Prime Video'},

    {'title': '24', 'language': 'tamil', 'genre': 'scifi', 'description': 'A scientist invents a time-traveling watch.', 'director': 'Vikram Kumar', 'rating': '7.9/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Enthiran', 'language': 'tamil', 'genre': 'scifi', 'description': 'A humanoid robot develops emotions.', 'director': 'S. Shankar', 'rating': '7.1/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Maanaadu', 'language': 'tamil', 'genre': 'scifi', 'description': 'A man is stuck in a time loop during a political event.', 'director': 'Venkat Prabhu', 'rating': '7.6/10', 'platform': 'SonyLIV'},
    {'title': 'Indru Netru Naalai', 'language': 'tamil', 'genre': 'scifi', 'description': 'Two friends find a time machine from the future.', 'director': 'R. Ravikumar', 'rating': '8.0/10', 'platform': 'Disney+ Hotstar'},
    {'title': '7aum Arivu', 'language': 'tamil', 'genre': 'scifi', 'description': 'A descendant of Bodhidharma must stop a biological war.', 'director': 'A.R. Murugadoss', 'rating': '6.2/10', 'platform': 'Zee5'},

    {'title': 'Pizza', 'language': 'tamil', 'genre': 'horror', 'description': 'A delivery boy experiences horror at a house.', 'director': 'Karthik Subbaraj', 'rating': '7.6/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Demonte Colony', 'language': 'tamil', 'genre': 'horror', 'description': 'Friends go into a haunted mansion to steal a necklace.', 'director': 'R. Ajay Gnanamuthu', 'rating': '7.0/10', 'platform': 'Sun NXT'},
    {'title': 'Pisaasu', 'language': 'tamil', 'genre': 'horror', 'description': 'A man is haunted by the spirit of a girl he tried to save.', 'director': 'Mysskin', 'rating': '7.5/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Aval', 'language': 'tamil', 'genre': 'horror', 'description': 'A neurosurgeon and his wife find their new neighbors haunted.', 'director': 'Milind Rau', 'rating': '6.8/10', 'platform': 'Netflix'},
    {'title': 'Yaavarum Nalam', 'language': 'tamil', 'genre': 'horror', 'description': 'A TV soap opera mirrors the events in a man\'s family.', 'director': 'Vikram Kumar', 'rating': '7.3/10', 'platform': 'Amazon Prime Video'},

    {'title': 'Ponniyin Selvan: I', 'language': 'tamil', 'genre': 'fantasy', 'description': 'An epic saga of the Chola dynasty.', 'director': 'Mani Ratnam', 'rating': '7.6/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Imsai Arasan 23rd Pulikecei', 'language': 'tamil', 'genre': 'fantasy', 'description': 'A satirical take on kings and historical myths.', 'director': 'Chimbu Deven', 'rating': '7.8/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Aayirathil Oruvan', 'language': 'tamil', 'genre': 'fantasy', 'description': 'A search for a lost Chola prince leads to a hidden civilization.', 'director': 'Selvaraghavan', 'rating': '8.1/10', 'platform': 'Sun NXT'},
    {'title': 'Iruvar', 'language': 'tamil', 'genre': 'fantasy', 'description': 'A fictionalized take on the life of movie stars in politics.', 'director': 'Mani Ratnam', 'rating': '8.4/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Kaashmora', 'language': 'tamil', 'genre': 'fantasy', 'description': 'A fraudster ends up in a haunted palace with ancient warriors.', 'director': 'Gokul', 'rating': '5.4/10', 'platform': 'Disney+ Hotstar'},

    # Kannada Movies
    {'title': 'K.G.F: Chapter 1', 'language': 'kannada', 'genre': 'action', 'description': 'A gangster aims to control the gold mines.', 'director': 'Prashanth Neel', 'rating': '8.2/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Kantara', 'language': 'kannada', 'genre': 'action', 'description': 'A conflict between a man and forest officials over tradition.', 'director': 'Rishab Shetty', 'rating': '8.3/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Mufti', 'language': 'kannada', 'genre': 'action', 'description': 'An undercover cop infiltrates a crime boss\'s inner circle.', 'director': 'Narthan', 'rating': '8.0/10', 'platform': 'Zee5'},
    {'title': 'Tagaru', 'language': 'kannada', 'genre': 'action', 'description': 'A face-off between a tough cop and a underworld don.', 'director': 'Duniya Soori', 'rating': '7.7/10', 'platform': 'Sun NXT'},
    {'title': 'Ugramm', 'language': 'kannada', 'genre': 'action', 'description': 'A man with a violent past tries to lead a normal life.', 'director': 'Prashanth Neel', 'rating': '8.0/10', 'platform': 'Voot'},

    {'title': 'Kirik Party', 'language': 'kannada', 'genre': 'comedy', 'description': 'A group of students navigate college life.', 'director': 'Rishab Shetty', 'rating': '8.0/10', 'platform': 'Voot'},
    {'title': 'Bell Bottom', 'language': 'kannada', 'genre': 'comedy', 'description': 'A detective in the 80s solves unusual thefts.', 'director': 'Jayatheertha', 'rating': '8.0/10', 'platform': 'Sun NXT'},
    {'title': 'First Rank Raju', 'language': 'kannada', 'genre': 'comedy', 'description': 'A nerd struggles to adapt to the real world.', 'director': 'Naresh Kumar', 'rating': '7.4/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Humble Politician Nograj', 'language': 'kannada', 'genre': 'comedy', 'description': 'A narcissistic politician does anything to stay in power.', 'director': 'Saad Khan', 'rating': '7.3/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Rama Rama Re', 'language': 'kannada', 'genre': 'comedy', 'description': 'A convict and his hangman end up on a road trip.', 'director': 'D. Satya Prakash', 'rating': '8.2/10', 'platform': 'Amazon Prime Video'},

    {'title': 'Lucia', 'language': 'kannada', 'genre': 'scifi', 'description': 'A man uses a pill to live his dream life.', 'director': 'Pawan Kumar', 'rating': '8.3/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Operation Alamelamma', 'language': 'kannada', 'genre': 'scifi', 'description': 'A clerk gets stuck in a tech-related crime.', 'director': 'Suni', 'rating': '7.2/10', 'platform': 'Zee5'},
    {'title': 'Blink', 'language': 'kannada', 'genre': 'scifi', 'description': 'A man discovers he can control time through his eyes.', 'director': 'Srinidhi Bengaluru', 'rating': '8.0/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Aatagara', 'language': 'kannada', 'genre': 'scifi', 'description': 'Ten people are stranded on an island with high-tech traps.', 'director': 'K.M. Chaitanya', 'rating': '7.5/10', 'platform': 'Sun NXT'},
    {'title': 'Man Of The Match', 'language': 'kannada', 'genre': 'scifi', 'description': 'A filmmaker creates chaos during an audition using tech.', 'director': 'D. Satya Prakash', 'rating': '6.4/10', 'platform': 'Amazon Prime Video'},

    {'title': 'Rangitaranga', 'language': 'kannada', 'genre': 'horror', 'description': 'A novelist uncovers secrets in his ancestral village.', 'director': 'Anup Bhandari', 'rating': '8.2/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Shhh!', 'language': 'kannada', 'genre': 'horror', 'description': 'A film crew encounters a ghost in a remote location.', 'director': 'Upendra', 'rating': '8.1/10', 'platform': 'YouTube'},
    {'title': 'Aake', 'language': 'kannada', 'genre': 'horror', 'description': 'A single mother experiences paranormal activity in a hospital.', 'director': 'K.M. Chaitanya', 'rating': '6.8/10', 'platform': 'Netflix'},
    {'title': '6-5=2', 'language': 'kannada', 'genre': 'horror', 'description': 'Found footage of a trekking trip gone wrong.', 'director': 'KS Ashoka', 'rating': '6.5/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Apthamitra', 'language': 'kannada', 'genre': 'horror', 'description': 'A psychiatrist treats a woman obsessed with an ancient spirit.', 'director': 'P. Vasu', 'rating': '8.0/10', 'platform': 'Disney+ Hotstar'},

    {'title': 'Vikrant Rona', 'language': 'kannada', 'genre': 'fantasy', 'description': 'A police officer investigates a haunted village.', 'director': 'Anup Bhandari', 'rating': '7.0/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Babruvahana', 'language': 'kannada', 'genre': 'fantasy', 'description': 'The story of Arjuna and his son Babruvahana.', 'director': 'Hunsur Krishnamurthy', 'rating': '8.4/10', 'platform': 'YouTube'},
    {'title': 'Avatara Purusha', 'language': 'kannada', 'genre': 'fantasy', 'description': 'A fake exorcist gets caught in real black magic.', 'director': 'Suni', 'rating': '6.3/10', 'platform': 'Amazon Prime Video'},
    {'title': '777 Charlie', 'language': 'kannada', 'genre': 'fantasy', 'description': 'A lonely man finds meaning through a labrador dog.', 'director': 'Kiranraj K', 'rating': '8.7/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Gajakesari', 'language': 'kannada', 'genre': 'fantasy', 'description': 'A man discovers his past connection to an ancient warrior.', 'director': 'S. Krishna', 'rating': '6.5/10', 'platform': 'Disney+ Hotstar'},

    # English Movies
    {'title': 'Avengers: Endgame', 'language': 'english', 'genre': 'action', 'description': 'Heroes unite to reverse Thanos\' destruction.', 'director': 'Russo Brothers', 'rating': '8.4/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Mad Max: Fury Road', 'language': 'english', 'genre': 'action', 'description': 'A woman rebels against a tyrant in a wasteland.', 'director': 'George Miller', 'rating': '8.1/10', 'platform': 'Amazon Prime Video'},
    {'title': 'The Dark Knight', 'language': 'english', 'genre': 'action', 'description': 'Batman faces the Joker in Gotham.', 'director': 'Christopher Nolan', 'rating': '9.0/10', 'platform': 'Netflix'},
    {'title': 'John Wick', 'language': 'english', 'genre': 'action', 'description': 'An ex-hitman comes out of retirement.', 'director': 'Chad Stahelski', 'rating': '7.4/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Gladiator', 'language': 'english', 'genre': 'action', 'description': 'A Roman general seeks revenge against a corrupt emperor.', 'director': 'Ridley Scott', 'rating': '8.5/10', 'platform': 'Netflix'},

    {'title': 'Deadpool', 'language': 'english', 'genre': 'comedy', 'description': 'A mercenary with healing powers seeks revenge.', 'director': 'Tim Miller', 'rating': '8.0/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'The Grand Budapest Hotel', 'language': 'english', 'genre': 'comedy', 'description': 'The adventures of a concierge at a famous hotel.', 'director': 'Wes Anderson', 'rating': '8.1/10', 'platform': 'Disney+ Hotstar'},
    {'title': 'Superbad', 'language': 'english', 'genre': 'comedy', 'description': 'Two high school seniors try to buy alcohol for a party.', 'director': 'Greg Mottola', 'rating': '7.6/10', 'platform': 'Netflix'},
    {'title': 'The Hangover', 'language': 'english', 'genre': 'comedy', 'description': 'Three friends search for their missing groom in Vegas.', 'director': 'Todd Phillips', 'rating': '7.7/10', 'platform': 'Netflix'},
    {'title': 'Mean Girls', 'language': 'english', 'genre': 'comedy', 'description': 'A new student joins a group of popular girls.', 'director': 'Mark Waters', 'rating': '7.1/10', 'platform': 'Amazon Prime Video'},

    {'title': 'The Matrix', 'language': 'english', 'genre': 'scifi', 'description': 'A hacker discovers reality is a simulation.', 'director': 'The Wachowskis', 'rating': '8.7/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Inception', 'language': 'english', 'genre': 'scifi', 'description': 'A thief enters dreams to steal secrets.', 'director': 'Christopher Nolan', 'rating': '8.8/10', 'platform': 'Netflix'},
    {'title': 'Interstellar', 'language': 'english', 'genre': 'scifi', 'description': 'Explorers travel through a wormhole to save humanity.', 'director': 'Christopher Nolan', 'rating': '8.7/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Arrival', 'language': 'english', 'genre': 'scifi', 'description': 'Linguists communicate with aliens.', 'director': 'Denis Villeneuve', 'rating': '7.9/10', 'platform': 'Netflix'},
    {'title': 'Blade Runner 2049', 'language': 'english', 'genre': 'scifi', 'description': 'A blade runner uncovers a long-buried secret.', 'director': 'Denis Villeneuve', 'rating': '8.0/10', 'platform': 'Netflix'},

    {'title': 'The Conjuring', 'language': 'english', 'genre': 'horror', 'description': 'Investigators help a family haunted by a dark presence.', 'director': 'James Wan', 'rating': '7.5/10', 'platform': 'Netflix'},
    {'title': 'Hereditary', 'language': 'english', 'genre': 'horror', 'description': 'A family is haunted after their grandmother\'s death.', 'director': 'Ari Aster', 'rating': '7.3/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Get Out', 'language': 'english', 'genre': 'horror', 'description': 'A man discovers a sinister secret about his girlfriend\'s family.', 'director': 'Jordan Peele', 'rating': '7.7/10', 'platform': 'Amazon Prime Video'},
    {'title': 'A Quiet Place', 'language': 'english', 'genre': 'horror', 'description': 'A family must live in silence to avoid monsters.', 'director': 'John Krasinski', 'rating': '7.5/10', 'platform': 'Netflix'},
    {'title': 'It', 'language': 'english', 'genre': 'horror', 'description': 'Seven kids face a shape-shifting monster.', 'director': 'Andy Muschietti', 'rating': '7.3/10', 'platform': 'Netflix'},

    {'title': 'The Lord of the Rings', 'language': 'english', 'genre': 'fantasy', 'description': 'A hobbit goes on a journey to destroy a ring.', 'director': 'Peter Jackson', 'rating': '8.8/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Harry Potter', 'language': 'english', 'genre': 'fantasy', 'description': 'A boy discovers he is a wizard.', 'director': 'Chris Columbus', 'rating': '7.6/10', 'platform': 'Amazon Prime Video'},
    {'title': 'Spirited Away', 'language': 'english', 'genre': 'fantasy', 'description': 'A girl enters a world ruled by spirits.', 'director': 'Hayao Miyazaki', 'rating': '8.6/10', 'platform': 'Netflix'},
    {'title': 'Pan\'s Labyrinth', 'language': 'english', 'genre': 'fantasy', 'description': 'A girl escapes to a mystical world during a war.', 'director': 'Guillermo del Toro', 'rating': '8.2/10', 'platform': 'Netflix'},
    {'title': 'The Shape of Water', 'language': 'english', 'genre': 'fantasy', 'description': 'A woman forms a relationship with an amphibious creature.', 'director': 'Guillermo del Toro', 'rating': '7.3/10', 'platform': 'Disney+ Hotstar'},
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
