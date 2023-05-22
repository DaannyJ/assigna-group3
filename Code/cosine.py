'''
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from buzz_words_list import *
import numpy as np
from nltk import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer
from colorama import Fore, Style
from termcolor import colored

df = pd.read_csv('C:/Users/jonat/Documents/GitHub/assigna-group3/Code/preprocessed_swe_1.csv')  # Replace 'your_dataframe.csv' with the actual filename
pd.set_option('display.max_colwidth', 100)

mono_buzz = buzz_monograms()
bi_buzz = buzz_bigrams()


# Combine the descriptions and word list
descriptions = df['description'].tolist()
word_list_strings = [' '.join(tup) for tup in bi_buzz]
word_list = mono_buzz + word_list_strings
documents = descriptions + mono_buzz #word_list  #_strings

vectorizer = TfidfVectorizer() # NY
#vectorizer = CountVectorizer()
vectorized_documents = vectorizer.fit_transform(documents)
similarity_matrix = cosine_similarity(vectorized_documents[-len(word_list):], vectorized_documents[:-len(word_list)])

# Extract similarity scores for each description
description_scores = []
for i, word_tuple in enumerate(word_list):
    similar_desc_indices = similarity_matrix[i].argsort()[:-2:-1]
    similar_scores = similarity_matrix[i][similar_desc_indices]
    description_scores.extend(similar_scores)

# Calculate the average score of all descriptions
average_score = np.mean(description_scores)

print("Description Index\tHeadline\t\t\tSimilarity Score")
print("--------------------------------------------------------------")
for i, (headline, score) in enumerate(zip(df['headline'], description_scores), 1):
    print(f"{i}\t\t\t{headline}\t\t\t{score}")

print(f"\nAverage score of all descriptions: {average_score}")

# Choose a specific description by index
selected_index = int(input("\nEnter the index of the description you want to choose: "))
selected_description = df.iloc[selected_index]['description']


print("\nSelected description:")
print(selected_description)
'''

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from buzz_words_list import *
import numpy as np
from colorama import Fore, Style
from termcolor import colored
from excluded_words_list import *

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


print("Description Index\tHeadline\t\t\tSimilarity Score")
print("--------------------------------------------------------------")
for i, (headline, score) in enumerate(zip(df['headline'], description_scores), 1):
    print(f"{i}\t\t\t{headline}\t\t\t{score}")

print(f"\nAverage score of all descriptions: {average_score}")

# Choose a specific description by index
selected_index = int(input("\nEnter the index of the description you want to choose: "))
selected_description = df.iloc[selected_index]['description']

print("\nSelected description:")
print(selected_description)
