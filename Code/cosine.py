import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from excluded_words_list import *
import numpy as np

df = pd.read_csv('C:/Users/jonat/Documents/GitHub/assigna-group3/Code/preprocessed_swe_1.csv')  # Replace 'your_dataframe.csv' with the actual filename
ex_mono = excluded_monograms()
ex_bi = excluded_bigrams()
word_list = ex_mono + ex_bi
descriptions = df['description'].tolist()
documents = descriptions + word_list
documents = [str(document) for document in documents]

vectorizer = CountVectorizer()
vectorized_documents = vectorizer.fit_transform(documents)
similarity_matrix = cosine_similarity(vectorized_documents[-len(word_list):], vectorized_documents[:-len(word_list)])

# Extract similarity scores for each description
description_scores = []
for i, word in enumerate(word_list):
    similar_desc_indices = similarity_matrix[i].argsort()[:-2:-1]
    similar_scores = similarity_matrix[i][similar_desc_indices]
    description_scores.extend(similar_scores)

# Calculate the average score of all descriptions
average_score = np.mean(description_scores)

print("Similarity scores for each description:")
for i, score in enumerate(description_scores):
    print(f"Description {i+1}: {score}")
print(f"\nAverage score of all descriptions: {average_score}")


