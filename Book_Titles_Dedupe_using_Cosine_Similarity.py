# Problem Statement: I had wishlist from two different sources- Goodreads and Amazon
# I want to de-dupe the data between the two
# Owing to different publishers and formats the name could have been sligtly different
#  For example say :
#The Remains of the Day [Hardcover] at good reads
# Ishiguro, Kazuo The Remains of the Day by Kazuo at Amazon


# To dedupe am using all-MiniLM-L6-v2 to vectorize the the book titles

# Then I computed cosine similarity scores among the two models



# %pip install sentence-transformers -q



from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')

# Two lists of words
word1 = ['The New York Trilogy', 'A Body at a Boarding School: A 1920s Mystery ', 'Les Miserables', 'The Alienist', 'The Journey to the West', 'Meddling Kids: The Wand Collection', "If on a Winter's Night a Traveler", "Best of Wodehouse, The (Everyman's Library P G WODEHOUSE)", 'The Real Life of Sebastian Knight (Vintage International)', 'CITY & THE CITY', 'V.', "Waterland (Everyman's Library CLASSICS)", 'The Remains of the Day [Hardcover] Ishiguro, Kazuo', 'Love In The Time Of Cholera', "My Name is Red (Everyman's Library CLASSICS)", "Beloved (Everyman's Library CLASSICS)", 'Ulysses', 'Love in the Time of Cholera', 'Baudolino', 'Nobody Move: A Novel', 'Jerusalem', 'Border Trilogy', 'In Cold Blood', 'LONESOME DOVE', 'Morality Play (Norton Paperback Fiction)', "Butcher's Crossing", "Butcher's Crossing", 'No Country for Old Men', 'Suttree', 'Middlesex', 'The Marriage Plot: A Novel', 'Corrections: A Novel', "Gulliver's Travels", 'Robinson Crusoe', 'Invention Of Morel: Or a History of Food and Its Preparation in Ancient Times', 'Noctuary', "Yiddish Policemen's Union: A Novel", 'Notes from Underground ', 'The New Annotated Strange Case of Dr. Jekyll and Mr. Hyde', 'House of Leaves: The Remastered Full-Color Edition', "Gravity's Rainbow : Penguin Classics Del", 'Pride & Prejudice : Penguin Classics Del', 'Wuthering Heights : Penguin Classics Del', 'The Sun Also Rises: (Penguin Classics De', 'Heart of Darkness (Classics Deluxe Ed)', 'White Noise : Penguin Classics Deluxe Ed', 'The Aeneid', "Histories (Everyman's Library CLASSICS)", 'Area X', 'The Golem (European Classics)', "The Sound and the Fury: The Corrected Text with Faulkner's Appendix (Modern Library 100 Best Novels)", 'A Fable (Vintage International)', 'AS I LAY DYING OPRAH SUMMER 05', 'Intruder In The Dust', 'The Reivers', 'Requiem for a Nun', 'Light in August: The Corrected Text', 'The Unvanquished: The Corrected Text (Vintage International)', 'The Town (Vintage International)', 'The Mansion (Vintage International)', 'The Hamlet (Vintage International)', 'Swamplandia! (Vintage Contemporaries)', 'LINCOLN', '2666: A Novel', 'Naked Lunch', 'The 7th Function of Language', 'The Pancatantra', 'The Book of Genesis', 'Divine Comedy: Inferno, Purgatorio, Paradiso', 'The Last Temptation Of Christ', 'Golem and the Jinni: A Novel', 'Savage Detectives', 'Cloud Atlas', 'Conference of The Birds (Penguin Classics)', 'Amerika: The Missing Person: A New Translation, Based on the Restored Text (The Schocken Kafka Library)', "Midnight's Children (Everyman's Library CLASSICS)", "The New Testament (Everyman's Library CLASSICS)", 'The Code of the Woosters', 'Kappa', 'Hopscotch', 'Abhijnanashakuntalam (PB)', 'Raghuvamsam', 'Gormenghast Trilogy', 'Against the Day', 'The Mahabharata', 'The Night Ocean', 'The Maltese Falcon', 'The Master and Margarita', 'Crime and Punishment', 'Death on Gokumon Island', 'A Journey to the Centre of the Earth', 'Republic', 'The New Annotated Frankenstein', 'The Name of the Rose', 'Antony and Cleopatra', 'Play : Rosencrantz & Guildenstern are De', 'Melmoth the Wanderer (Penguin Classics)', 'Phantom of the Opera ', 'Kraken', 'Annihilation: A Novel', 'Perdido Street Station', 'Mysteries of Paris (Penguin Classics) [Paperback] Sue, Eugene', 'Canterbury Tales (No Fear)', 'No Fear Shakespeare: Sonnets', 'Come Tomorrow : and other tales of Bangalore terror', 'The Epic of Gilgamesh', 'Five Decembers', 'The Secret History', 'The Investigation', 'The Shootist', "Butcher's Crossing", 'No Country for Old Men', 'The Glass Key', 'The Third Man', 'The Postman Always Rings Twice', 'And Then There Were None', 'Moby Dick', 'The Monk', 'The Italian', 'The Hunchback of Notre Dame', 'The Left Hand of Darkness']
word2 = ['New York Trilogy', 'A Body at a Boarding School', 'Les Miserables by Victor Hugo','V.', 'Waterland', 'The Remains of the Day by Kazuo', 'Hero the man', 'Sequence', 'The Last Man', 'Dracula']

#Compute embedding for both lists
embeddings1 = model.encode(word1, convert_to_tensor=True)
embeddings2 = model.encode(word2, convert_to_tensor=True)

#Compute cosine-similarities
cosine_scores = util.cos_sim(embeddings1, embeddings2)
print(cosine_scores)

for i in range(len(word1)):
  for j in range(len(word2)):
    if not(i==j):
      if cosine_scores[i][j]>0.50:
        print(word1[i],word2[j])