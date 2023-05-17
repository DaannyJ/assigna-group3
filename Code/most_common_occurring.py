import pandas as pd
import nltk
from collections import Counter
from nltk import ngrams
from nltk.tokenize import word_tokenize

def get_top_grams(df, row_limit, num_grams):
    # Limit the DataFrame to the specified number of rows
    df = df.head(row_limit)

    # Tokenize each description
    tokenized_descriptions = [word_tokenize(desc.lower()) for desc in df['description.text']]

    # Create a list to store all monograms and bigrams
    all_grams = []

    # Extract monograms and bigrams from tokenized descriptions
    for desc in tokenized_descriptions:
        monograms = desc
        bigrams = list(ngrams(desc, 2, pad_left=True, pad_right=True))
        all_grams.extend(monograms + bigrams)

    # Count the occurrences of each monogram and bigram
    gram_counts = Counter(all_grams)

    # Get the most common monograms and bigrams
    top_grams = gram_counts.most_common(num_grams)

    return top_grams

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


##GAMLA##
'''
import pandas as pd
import nltk
from collections import Counter
from nltk import ngrams
from nltk.tokenize import word_tokenize


# Load the dataset into a pandas DataFrame
df = pd.read_csv('fil här')
#print(df.head)
# Set the desired row limit
row_limit = 10000

# Limit the DataFrame to the specified number of rows
df = df.head(row_limit)

# Tokenize each description
tokenized_descriptions = [word_tokenize(desc.lower()) for desc in df['description.text']]

# Create a list to store all monograms and bigrams
all_grams = []

# Extract monograms and bigrams from tokenized descriptions
for desc in tokenized_descriptions:
    monograms = desc
    bigrams = list(ngrams(desc, 2, pad_left=True, pad_right=True))
    all_grams.extend(monograms + bigrams)

# Count the occurrences of each monogram and bigram
# ändrat från allgrams till bara bigrams för att se
gram_counts = Counter(all_grams)

# Get the most common 10 monograms and bigrams
top_10_grams = gram_counts.most_common(100)

# Print the results
for gram, count in top_10_grams:
    print(gram, ":", count)
'''