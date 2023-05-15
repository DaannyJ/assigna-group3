### HELLO!!
### This is code that tokenizes, stems, and removes stopwords from a column in a csv 

import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# Load CSV file
data = pd.read_csv('C:/Users/carlt/Documents/TIG326/kod till projektet/datasets/2022_good_cols_10000.csv')

# manually added stopwords HERE. Needs to be filled in and added into the function
# manual_stopwords = ZANAPLATSEN.dict.deez

# Tokenization, stemming, and stopword removal
def preprocess_swedish_text(text):
    tokens = word_tokenize(str(text), language='swedish')  # Convert to string if not already
    stop_words = set(stopwords.words('swedish'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    stemmer = SnowballStemmer('swedish')
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    return stemmed_tokens

# # # use this if you want to apply preprocessing function to "description.text" column and write to new column
# data['preprocessed_text'] = data['description.text'].apply(preprocess_swedish_text)

# # # use this if you want to  REPLACE "description.text" column with the preprocessed text column
data['description.text'] = data['description.text'].apply(preprocess_swedish_text)


# Write preprocessed data to a new CSV file
data.to_csv("preprocessed_data_2.csv", index=False)
