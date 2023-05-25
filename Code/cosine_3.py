import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Assuming these functions are defined in buzz_words_list module
from buzz_words_list import buzz_monograms, buzz_bigrams


# Read the CSV file
df = pd.read_csv('C:/Users/jonat/Documents/GitHub/assigna-group3/Code/preprocessed_swe_1.csv')
pd.set_option('display.max_colwidth', 100)

# Get descriptions and word list
descriptions = df['description'].tolist()

# Import buzzwords monograms
mono_buzz = buzz_monograms()

# Import buzzwords bigrams
bi_buzz = buzz_bigrams()

# Create bigrams from tuples to a list
bigrams = [' '.join(tup) for tup in bi_buzz]

# Vectorize the monograms
vectorizer_monograms = TfidfVectorizer()
vectorized_monograms_buzz = vectorizer_monograms.fit_transform(mono_buzz)
vectorized_monograms_descriptions = vectorizer_monograms.transform(descriptions)

# Calculate similarity between monograms and descriptions
similarity_monograms = cosine_similarity(vectorized_monograms_descriptions, vectorized_monograms_buzz)

# Extract similarity scores and feature names for each description
description_scores_monograms = similarity_monograms.max(axis=1)
monogram_feature_names = vectorizer_monograms.get_feature_names()

# Vectorize the bigrams
vectorizer_bigrams = TfidfVectorizer(vocabulary=bigrams, ngram_range=(2, 2))
vectorized_bigrams = vectorizer_bigrams.fit_transform(descriptions)

# Calculate the scores and feature names for each bigram
description_scores_bigrams = []
bigram_feature_names = vectorizer_bigrams.get_feature_names()
for i, description in enumerate(descriptions):
    vectorized_description = vectorized_bigrams[i]
    bigram_scores = []
    bigrams_used = []
    for feature_index, count in zip(vectorized_description.indices, vectorized_description.data):
        bigram = bigram_feature_names[feature_index]
        words = bigram.split()
        if words[0] in description and words[1] in description:
            bigram_scores.append(count)
            bigrams_used.append(bigram)
    if bigram_scores:
        description_scores_bigrams.append(max(bigram_scores))
    else:
        description_scores_bigrams.append(0)

    print(f"Description {i+1}:")
    print("Monogram Score:", description_scores_monograms[i])
    print("Monograms:", [monogram_feature_names[idx] for idx in vectorized_monograms_descriptions[i].indices])
    print("Bigram Score:", description_scores_bigrams[i])
    print("Bigrams:", bigrams_used)
    print()
