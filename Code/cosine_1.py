

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from buzz_words_list import *
import numpy as np
from colorama import Fore, Style
from termcolor import colored
from excluded_words_list import *

def get_buzz():
    all_buzz = description_scores.tolist()
    
    return all_buzz

def get_avg_buzz():
    avg_buzz = average_score
    return avg_buzz

df = pd.read_csv('C:/Users/jonat/Documents/GitHub/assigna-group3/Code/preprocessed_swe_1.csv')
pd.set_option('display.max_colwidth', 100)



mono_buzz = buzz_monograms()
bi_buzz = buzz_bigrams()
'''
# Combine the descriptions and word list
descriptions = df['description'].tolist()
word_list_strings = [' '.join(tup) for tup in bi_buzz]
word_list = word_list_strings + mono_buzz
#print(word_list)

excluded_words = excluded_monograms()
excluded_combinations = excluded_bigrams()

documents = descriptions + word_list
'''

excluded_words = excluded_monograms()
excluded_combinations = excluded_bigrams()

# Combine the descriptions and word list
descriptions = df['description'].tolist()

# Exclude words from descriptions
filtered_descriptions = []
for description in descriptions:
    description_words = description.split()
    filtered_words = [word for word in description_words if word not in excluded_words and word not in excluded_combinations]
    filtered_description = ' '.join(filtered_words)
    filtered_descriptions.append(filtered_description)


word_list_strings = [' '.join(tup) for tup in excluded_combinations]
word_list = excluded_words + word_list_strings
documents = filtered_descriptions + word_list_strings
vectorizer = TfidfVectorizer()
vectorized_documents = vectorizer.fit_transform(documents)

# Calculate similarity between descriptions and word list
similarity_descriptions_word_list = cosine_similarity(vectorized_documents[:len(descriptions)], vectorized_documents[len(descriptions):])

# Extract similarity scores for each description
description_scores = similarity_descriptions_word_list.max(axis=1)

# Calculate the average score of all descriptions
average_score = np.mean(description_scores)

# Calculate the average score of all descriptions

max_headline_length = max(len(headline) for headline in df['headline'])
print("Description Index\tHeadline\t\t\tSimilarity Score")
print("--------------------------------------------------------------")
print("Description Index\tHeadline" + " "*(max_headline_length-8) + "\t\tSimilarity Score")
print("--------------------------------------------------------------")
for i, (headline, score) in enumerate(zip(df['headline'], description_scores), 1):
    print(f"{i}\t\t\t{headline.ljust(max_headline_length)}\t\t{score}")



print(f"\nAverage score of all descriptions: {average_score}")

# Choose a specific description by index
#selected_index = int(input("\nEnter the index of the description you want to choose: "))
#selected_description = df.iloc[selected_index]['description']

#print("\nSelected description:")
#print(selected_description) # för att välja en description och titta i den.

print(get_buzz())
print(get_avg_buzz())