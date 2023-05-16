### HELLO!!
### This is code that removes special characters and numbers, tokenizes, stems, and removes stopwords from a column in a csv 

import pandas as pd
import nltk
import string   # needed for punctuation removal
import re       # needed for numbers removal
# nltk.download('punkt')      # can be commented out after running for the first time
# nltk.download('stopwords')  # can be commented out after running for the first time
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

from Visualization import * # EDA for the preprocessing
from language_remover import language_remover # For removing non swedish ads

## Load DA CSV
data = pd.read_csv('C:/Users/carlt/Documents/TIG326/kod till projektet/datasets/sample_1000_per_year.csv', index_col=0)

visualize_data(data)
## Removing punctuation, numbers. Tokenization, stemming and stopword removal
def preprocess_swedish_text(text):
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation)) # replaces special characters with spaces
    text = text.translate(translator)   # applies it to the text

    text = re.sub(r'\d+', "", text)     # Removes numbers

    tokens = word_tokenize(str(text), language='swedish')  # Tokenizer. Str conversion needed or errors will happen
    stop_words = set(stopwords.words('swedish'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    stemmer = SnowballStemmer('swedish')
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    # return (stemmed_tokens)            ## TWO VARIANTS here
    return ' '.join(stemmed_tokens)     ## This one removes quotes between tokens. Reduces filesize a bit in the end

# call on the language_remover
swedish_ads = language_remover(data)

# Runs the preprocessor. REPLACES "description.text" column with the preprocessed text column
swedish_ads['description'] = swedish_ads['description'].apply(preprocess_swedish_text)    

visualize_data(swedish_ads)

print(swedish_ads)


# # # Write preprocessed data to a new CSV file
# data.to_csv("preprocessed_data_15.csv", index=False)

# pd.set_option('display.max_colwidth', 120)
# df = pd.DataFrame(data.description)
# print(df.head(20))