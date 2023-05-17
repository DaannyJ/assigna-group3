from collections import Counter
from nltk import ngrams
import pandas as pd

data = pd.read_csv('C:/Users/carlt/Documents/TIG326/kod till projektet/assigna-group3/code/preprocessed_swe_1.csv', index_col=0)

def get_top_grams(df, row_limit, num_grams):
    # Limit the DataFrame to the specified number of rows
    df = df.head(row_limit)

    # Create a list to store all monograms and bigrams
    all_grams = []

    # Extract monograms and bigrams from tokenized descriptions
    for desc in df['description']:
        grams = desc.split()
        all_grams.extend(grams)
    
    excluded_words = ['arbet', 'kund', 'sök', 'hos', 'tjänst', 'topwork', 'komm', 'medarbet', 'person', 'nya', 'erfaren', 'god', 'rätt', 'utveckl', 'roll', 'anställning', 'vill', 'ska', 'får', 'vikt', 'jobb', 'samt', 'båd', 'finn', 'krav', 'företag', 'kunskap', 'svensk', 'utmaning', 'tid', 'möj', 'mål', 'uppdrag', 'stor', 'hitt', 'körkort', 'rekrytering', 'trygg', 'bygg', 'erbjud', 'även', 'b', 'in', 'konsult', 'stött', 'sen', 'del', 'oavset', 'arbetsuppgift', 'meriter']

# Remove excluded words from all_grams
    all_grams = [gram for gram in all_grams if not any(word in gram for word in excluded_words)]


    # Count the occurrences of each monogram and bigram
    gram_counts = Counter(all_grams)

    # Get the most common monograms and bigrams
    top_grams = gram_counts.most_common(num_grams)

    return top_grams

top_grams = get_top_grams(data, 200, 50)
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