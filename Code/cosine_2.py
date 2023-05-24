import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from buzz_words_list import *
import numpy as np

from excluded_words_list import *


def filter_descriptions(descriptions, excluded_words, excluded_combinations):
    filtered_descriptions = []
    for description in descriptions:
        description_words = description.split()
        filtered_words = [word for word in description_words if word not in excluded_words and word not in excluded_combinations]
        filtered_description = ' '.join(filtered_words)
        filtered_descriptions.append(filtered_description)
    return filtered_descriptions


def calculate_cosine_scores(descriptions, word_list):
    vectorizer = TfidfVectorizer()
    vectorized_documents = vectorizer.fit_transform(descriptions + word_list)

    # Calculate similarity between descriptions and word list
    similarity_matrix = cosine_similarity(vectorized_documents[:-len(word_list)], vectorized_documents[-len(word_list):])

    # Extract similarity scores for each description
    description_scores = similarity_matrix.max(axis=1)

    return description_scores


def get_buzz_scores(df):
    mono_buzz = buzz_monograms()
    bi_buzz = buzz_bigrams()
    excluded_words = excluded_monograms()
    excluded_combinations = excluded_bigrams()

    descriptions = df['description'].tolist()

    filtered_descriptions = filter_descriptions(descriptions, excluded_words, excluded_combinations)

    word_list_strings = [' '.join(tup) for tup in bi_buzz]
    word_list = word_list_strings + mono_buzz

    description_scores = calculate_cosine_scores(filtered_descriptions, word_list)

    return description_scores


def get_average_buzz_score(description_scores):
    average_score = np.mean(description_scores)
    return average_score


def print_description_scores(df, description_scores):
    max_headline_length = max(len(headline) for headline in df['headline'])

    print("Description Index\tHeadline" + " " * (max_headline_length - 8) + "\t\tSimilarity Score")
    print("--------------------------------------------------------------")
    for i, (headline, score) in enumerate(zip(df['headline'], description_scores), 1):
        print(f"{i}\t\t\t{headline.ljust(max_headline_length)}\t\t{score}")

    print(f"\nAverage score of all descriptions: {get_average_buzz_score(description_scores)}")


def main():
    df = pd.read_csv('C:/Users/jonat/Documents/GitHub/assigna-group3/Code/preprocessed_swe_1.csv')
    pd.set_option('display.max_colwidth', 100)

    description_scores = get_buzz_scores(df)

    print_description_scores(df, description_scores)

    # Choose a specific description by index
    selected_index = int(input("\nEnter the index of the description you want to choose: "))
    selected_description = df.iloc[selected_index]['description']

    print("\nSelected description:")
    print(selected_description)


if __name__ == '__main__':
    main()
