from collections import Counter
from nltk import ngrams
import pandas as pd
import re

data = pd.read_csv('C:/Users/danie/Documents/assigna-group3/Code/preprocessed_swe_1.csv', index_col=0)

def get_top_grams(df, row_limit, num_grams):
    # Limit the DataFrame to the specified number of rows
    df = df.head(row_limit)

    # Create a list to store all monograms and bigrams
    all_grams = []

    # Extract monograms and bigrams from tokenized descriptions
    for desc in df['description']:
        words = re.findall(r'\w+', desc.lower())                 #<-----  
        #grams = list(ngrams(words, 1)) + list(ngrams(words, 2))  #<----- Denna gör att man får ut bigrams och monograms, men den lägger alla inom paranteser
        grams =list(ngrams(words, 2))                           #<------ Denna tar bara ut bigrams
        #grams = desc.split()                                    #<----- Dennna tar bara ut monograms
        all_grams.extend(grams)
    
    #Exkluderade ord, funkar bara om man söker efter monograms
    #Bigrams verkar dock mer intressanta
    excluded_words = [
       
                      'arbet', 'kund', 'sök', 'hos', 'tjänst', 'topwork', 'komm', 'medarbet', 'person', 'nya', 'erfaren', 'god', 
                      'rätt', 'utveckl', 'roll', 'anställning', 'vill', 'ska', 'får', 'vikt', 'jobb', 'samt', 'båd', 'finn', 'krav',      
                     'företag', 'kunskap', 'svensk', 'utmaning', 'tid', 'möj', 'mål', 'uppdrag', 'stor', 'hitt', 'körkort', 'rekrytering',
                     'trygg', 'bygg', 'erbjud', 'även', 'b', 'in', 'konsult', 'stött', 'sen', 'del', 'oavset', 'arbetsuppgift', 'meriter'
                     'gärn','ta','kräv','ser','triv','råd','övergå','tal','ger', 'lägg','dag', 'övr','–','idag','kunn','start','redan',   
                     'genom','hjälp','gill', 'såväl','tyck','sver','högt','få','sätt','andr', 'se','mer', 'enl','hel','via', 'www','år', 
                      'också','går','väx', '•','tillsamman','gör','olik', 'när', 'stockholm','patient','vid','engelsk', 'ge','organisation',
                      'lyck', 'därför', 'skrift','hög', 'sjukskötersk', 'https','läs','följ','elev', 'verksam', 'löp', '·','region','lön','fråg',
                                                               
                     ]

# Remove excluded words from all_grams
    all_grams = [gram for gram in all_grams if not any(word in gram for word in excluded_words)]

    # Count the occurrences of each monogram and bigram
    gram_counts = Counter(all_grams)

    # Get the most common monograms and bigrams
    top_grams = gram_counts.most_common(num_grams)

    return top_grams

top_grams = get_top_grams(data, 20000, 300)
for gram, count in top_grams:
    print(gram, ":", count)
for gram, count in top_grams:
    print(gram, end='')



'''
# Example usage:
# Load the dataset into a pandas DataFrame
df = pd.read_csv('file.csv')
# Set the desired row limit
row_limit = 10000
# Specify the number of top grams to retrieve
num_grams = 100

# Call the function
top_grams = get_top_grams(df, row_limit, num_grams)

# Print the results
for gram, count in top_grams:
    print(gram, ":", count)
'''