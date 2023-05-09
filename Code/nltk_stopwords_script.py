import pandas as pd
import nltk
from nltk.corpus import stopwords

# Load the dataset into a pandas DataFrame
df = pd.read_csv('2022_downsampled_10000.csv')
pd.set_option('max_columns', None)

# Load the Swedish stopwords list
swedish_stopwords = stopwords.words('swedish')

# Add the additional words to exclude
exclude_words = [['och', 'söker', 'sker', 'måste', 'all', 'bör’, ‘är', 'kommer', 'att', 'i', 'du', 'med', 'har', 'din', 'som', 'själv', 'det', '-', 'vi', 'en', 'för', 'av', 'på', 'till', 'inte', 'men', 'så', 'kan', 'om', 'eller', 'när', 'utan', 'vid', 'alla', 'blir', 'ett', 'mot', 'mycket', 'nu', 'sig', 'än', 'andra', 'bara', 'bli', 'både', 'där', 'dessa', 'dock', 'efter', 'genom', 'ha', 'hade', 'han', 'hans', 'hos', 'hur', 'in', 'inga', 'inom', 'inuti', 'ja', 'jag', 'ju', 'såsom', 't.ex.', 'bl.a.', 'd.v.s', 'enligt', 'mellan', 'ofta', 'ibland', 'många', 'behöva', 'också', 'även', 'dessutom', 'ytterligare', 'för det första', 'för det andra', 'tilläggas', 'slutligen', 'sist men inte minst', 'inledningsvis', 'omedelbart därefter', 'under tiden', 'samtidigt', 'efter', 'så småningom', 'efter ett tag', 'först', 'senare', 'tidigare', 'till sist', 'dels-dels', 'jämfört med', 'såsom', 'på samma sätt som', 'på så sätt', 'i likhet med', 'en likartad uppfattning', 'likartat', 'i sin tur', 'samtidigt', 'fördelarna', 'nackdelarna', 'däremot', 'men emellertid', 'dock', 'ändå', 'icke desto mindre', 'trots', 'trots allt', 'trots att', 'även om', 'i motsats till', 'å ena sidan', 'å andra sidan', 'när allt kommer omkring', 'en skillnad är', 'tvärtemot', 'tvärtom', 'i gengäld', 'såsom', 'till exempel', 'exempelvis', 'bland annat', 'det vill säga', 'illustrerar', 'illustreras', 'som ett exempel på', 'belyser', 'visar', 'här urskiljer sig', 'närmare bestämt', 'särskilt', 'i synnerhet', 'som', 'därför', 'således', 'detta beror på', 'alltså', 'på grund av', 'av detta skäl', 'beroende på', 'orsaken är', 'mot den bakgrunden', 'anledningen är', 'målet är att', 'detta går ut på att', 'i syfte att', 'som en följd av', 'härav följer', 'följaktligen', 'sålunda', 'resultatet blir', 'slutsatsen blir', 'vilket leder till', 'det(ta) beror på', 'och', 'det', 'att', 'i', 'en', 'jag', 'hon', 'som', 'han', 'på', 'den', 'med', 'var', 'sig', 'för', 'så', 'till', 'är', 'men', 'ett', 'om', 'hade', 'de', 'av', 'icke', 'mig', 'du', 'henne', 'då', 'sin', 'nu', 'har', 'inte', 'hans', 'honom', 'skulle', 'hennes', 'där', 'min', 'man', 'ej', 'vid', 'kunde', 'något', 'från', 'ut', 'efter', 'upp', 'vi', 'dem', 'vara', 'vad', 'över', 'än', 'dig', 'kan', 'sina', 'här', 'ha', 'mot', 'alla', 'under', 'någon', 'eller', 'allt', 'mycket', 'sedan', 'ju', 'denna', 'själv', 'detta', 'åt', 'utan', 'varit', 'hur', 'ingen', 'mitt', 'ni', 'bli', 'blev', 'oss', 'din', 'dessa', 'några', 'deras', 'blir', 'mina', 'samma', 'vilken', 'er', 'sådan', 'vår', 'blivit', 'dess', 'inom', 'mellan', 'sådant', 'varför', 'varje', 'vilka', 'ditt', 'vem', 'vilket', 'sitta', 'sådana', 'vart', 'dina', 'vars', 'vårt', 'våra', 'ert', 'era', 'vilkas']]
swedish_stopwords += exclude_words

# Define a function to remove stopwords from a piece of text
def remove_stopwords(text):
    if isinstance(text, str):
        tokens = nltk.word_tokenize(text.lower())
        filtered_tokens = [token for token in tokens if token not in swedish_stopwords]
        return ' '.join(filtered_tokens)
    else:
        return text

# Apply the function to the 'description.text' column
df['description.text'] = df['description.text'].apply(remove_stopwords)