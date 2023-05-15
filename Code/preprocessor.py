### Code that Tokenizes, stems, and removes stopwords.

import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# Load CSV file
data = pd.read_csv(('C:/Users/carlt/Documents/TIG326/kod till projektet/datasets/2022_good_cols_10000.csv'))

# Install and download necessary resources
nltk.download('stopwords')

# manually added stopwords HERE. Needs to be filled in and added into the function
manual_stopwords = 67890

# Tokenization, stemming, and stopword removal
def preprocess_swedish_text(text):
    tokens = word_tokenize(text, language='swedish')
    stop_words = set(stopwords.words('swedish'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    stemmer = SnowballStemmer('swedish')
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    return stemmed_tokens

# Apply preprocessing function to "description.text" column
data['preprocessed_text'] = data['description.text'].apply(preprocess_swedish_text)

# Write preprocessed data to a new csv file
data.to_csv("preprocessed_data.csv", index=False)