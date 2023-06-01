### HELLO!!
### This is code that removes special characters and numbers, tokenizes, stems, and removes stopwords from a column in a csv 
## Removing punctuation, numbers. Tokenization, stemming and stopword removal'
import nltk
def preprocess_swedish_text(text):

    import string   # needed for punctuation removal
    import re       # needed for numbers removal
    nltk.download('punkt')      # can be commented out after running for the first time
    nltk.download('stopwords')  # can be commented out after running for the first time
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    from nltk.stem.snowball import SnowballStemmer
    
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation)) # replaces special characters with spaces
    text = text.translate(translator)   # applies it to the text

    
    text = re.sub(r'[\d+]', "", text)     # Removes numbers
    

    tokens = word_tokenize(str(text), language='swedish')  # Tokenizer. Str conversion needed or errors will happen
    stop_words = set(stopwords.words('swedish'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    stemmer = SnowballStemmer('swedish')
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    return (stemmed_tokens)            ## TWO VARIANTS here
    # return ' '.join(stemmed_tokens)     ## This one removes quotes between tokens