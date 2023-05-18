from collections import Counter
from nltk import ngrams
import pandas as pd
import re
from excluded_words_list import *
from buzz_words_list import *

data = pd.read_csv('C:/Users/carlt/Documents/TIG326/kod till projektet/assigna-group3/code/preprocessed_swe_1.csv')

def get_top_words_and_combinations(df, row_limit, num_words, num_combinations):
    # Limit the DataFrame to the specified number of rows
    df = df.head(row_limit)

    # Create lists to store all words and combinations
    all_words = []
    all_combinations = []

    # Extract words and combinations from tokenized descriptions
    for desc in df['description']:
        words = re.findall(r'\w+', desc.lower())
        all_words.extend(words)
        combinations = list(ngrams(words, 2))
        all_combinations.extend(combinations)

    # Excluded words and combinations are stored within functions in separate files
    # These are stored in excluded_words_list.py
    excluded_words = excluded_monograms()
    excluded_combinations = excluded_bigrams()
    # Buzz mono and bigrams are stored in buzz_words_list.py
    buzz_words = buzz_monograms()
    buzz_combinations = buzz_bigrams()

    # Remove excluded words and combinations. These are found in excluded_words
    all_words = [word for word in all_words if word not in excluded_words]
    all_combinations = [combination for combination in all_combinations if combination not in excluded_combinations]

    # Remove excluded words and combinations and also remove words in the buzz_words_list.py
    # all_words = [word for word in all_words if word not in excluded_words and word not in buzz_words]
    # all_combinations = [combination for combination in all_combinations if combination not in excluded_combinations and combination not in buzz_combinations]



    # Count the occurrences of each word and combination
    word_counts = Counter(all_words)
    combination_counts = Counter(all_combinations)

    # Get the most common words and combinations
    top_words = word_counts.most_common(num_words)
    top_combinations = combination_counts.most_common(num_combinations)

    return top_words, top_combinations


top_words, top_combinations = get_top_words_and_combinations(data, 10000, 100, 100)

print("Most common words:")
for word, count in top_words:
    print(f"'{word}',")
print()
print("Most common two-word combinations:")
for combination, count in top_combinations:
    print(combination, end=',\n')

