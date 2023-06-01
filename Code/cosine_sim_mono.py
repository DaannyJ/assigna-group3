import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# from buzz_words_list import buzz_monograms
import numpy as np


def buzz_monograms():
     return [
'jisasdjiasdji',
'kodkoaasdsdkod']

df = pd.read_csv('C:/Users/danie/Documents/assigna-group3/Code/preprocessed_swe_1.csv')  # Replace 'your_dataframe.csv' with the actual filename

descriptions = df['description']


#Vectorize the data
vectorizer = CountVectorizer()
vectorized_documents = vectorizer.fit_transform(descriptions)

# Get the buzzwords
word_list = buzz_monograms()

# Vectorize the buzzwords
vectorized_buzzwords = vectorizer.transform(word_list)

# Calculate cosine similarity between buzzwords and descriptions
similarity_matrix = cosine_similarity(vectorized_buzzwords, vectorized_documents)

# Extract similarity scores for each description
average_scores = similarity_matrix.mean(axis=0)
n = 0
# Print the average score for each description
for i, score in enumerate(average_scores):
        print(f"Description {i}: Average Score = {score}")
        if score != 0.0:
                n += 1
print(n, "st träffar")
# Choose a specific description by index
selected_index = int(input("\nEnter the index of the description you want to choose: "))
selected_description = df.iloc[selected_index]['headline']
print(f"\nSelected description: {selected_description}, {score}")
