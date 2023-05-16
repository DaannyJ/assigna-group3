### HELLO!!
### This is code that tokenizes, stems, and removes stopwords from a column in a csv 

import pandas as pd
import nltk
nltk.download('punkt')      # can be commented out or removed after running for the first time
nltk.download('stopwords')  # can be commented out or removed after running for the first time
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import matplotlib.pyplot as plt

## Load your CSV
data = pd.read_csv('fil')

# manual_stopwords was previously called exclude_words. This list needs to be checked TOGETHER
# manual_stopwords = [
#     'och', 'och/eller', 'tjänst', 'hemtjänst', 'skicka', 'kund', 'verksamma', 'bil', 'deltid', 'barnen', 'täby', 'hsb', 'telefon', 'hand', 'hjälpa',
#     'henån', 'for', 'omsorg', 'familjen', 'vikariat', 'emot', 'medan','perfekta','söker', 'sker', 'måste', 'all', 'bör', 'kommer','i', 'du', 'har', 'din', 'själv', 'det', '-', 'vi', 'av', 'på', 'inte', 'men', 'kan', 'om', 'eller', 'när', 'utan', 'vid', 'alla', 'blir', 'mot', 'mycket', 'nu',
#     'än', 'andra', 'bara', 'bli', 'både', 'där', 'dessa', 'dock','genom', 'ha', 'hade', 'han', 'hans', 'hos', 'hur', 'in', 'inga', 'inom',
#     'inuti', 'ja', 'jag', 'ju', 't.ex.', 'bl.a.', 'd.v.s', 'enligt','mellan', 'ofta', 'ibland', 'många', 'behöva', 'också', 'även', 'dessutom',
#     'ytterligare', 'för det första', 'för det andra', 'tilläggas', 'slutligen','sist men inte minst', 'inledningsvis', 'omedelbart därefter', 'under tiden',
#     'samtidigt', 'efter', 'så småningom', 'efter ett tag', 'först', 'senare','tidigare', 'till sist', 'dels-dels', 'jämfört med', 'såsom',
#     'på samma sätt som', 'på så sätt', 'i likhet med', 'en likartad uppfattning','likartat', 'i sin tur', 'fördelarna', 'nackdelarna', 'däremot',
#     'men emellertid', 'ändå', 'icke desto mindre', 'trots', 'trots allt','trots att', 'även om', 'i motsats till', 'å ena sidan', 'å andra sidan',
#     'när allt kommer omkring', 'en skillnad är', 'tvärtemot', 'tvärtom','i gengäld', 'till exempel', 'exempelvis', 'bland annat',
#     'det vill säga', 'illustrerar', 'illustreras', 'som ett exempel på', 'belyser','visar', 'här urskiljer sig', 'närmare bestämt', 'särskilt', 'i synnerhet', 
#     'som', 'därför', 'således', 'detta beror på', 'alltså', 'på grund av', 'av detta skäl', 'beroende på', 'orsaken är', 'mot den bakgrunden', 
#     'anledningen är', 'målet är att', 'detta går ut på att', 'i syfte att','som en följd av', 'härav följer', 'följaktligen', 'sålunda', 'resultatet blir', 
#     'slutsatsen blir', 'vilket leder till', 'det(ta) beror på', 'att','en', 'hon', 'den', 'med', 'var', 'sig', 'för', 'så', 'till', 'är', 'ett', 'de', 'icke', 'mig',
#     'henne', 'då', 'sin', 'honom', 'skulle', 'hennes','min', 'man', 'ej', 'kunde', 'något', 'från', 'ut', 'upp', 'dem', 'vara', 'vad', 'över', 'dig', 'sina', 'här', 
#     'under', 'någon', 'allt', 'sedan', 'denna', 'detta', 'åt', 'varit', 'ingen', 'mitt', 'ni', 'blev', 'oss', 'några', 'deras', 'mina', 'samma', 'vilken', 'er', 'sådan', 'vår', 
#     'blivit', 'dess', 'sådant', 'varför', 'varje', 'vilka', 'ditt', 'vem', 'vilket', 'sitta', 'sådana', 'vart', 'dina', 'vars', 'vårt', 'våra', 'ert', 
#     'era', 'vilkas', 'samt', 'erfarenhet', 'arbeta', 'vill', 'arbetsuppgifter', 'arbete','arbetar', 'gärna', 'ska', 'god', 'ansökan', 'finns', 'utbildning', 'ser', 'person',
#     'ca', 'arbetet', 'tjänsten', 'skall', 'goda', 'olika', 'företag', 'ab', 'år', 'ingår', 'kunder', 'stor', 'medarbetare', 'erbjuder', 'kvalifikationer', 'krav', 'kunna', 'and', 
#     'nya', 'kunskaper', 'förmåga', 'innebär', 'personal', 'bra', 'behöver', 'sverige', 'via', 'mer', 'års', 'the', 'personer', 'barn', 'hela', 'självständigt', 'tillsammans', 
#     'stockholm', 'del', 'uppdrag', 'får', 'kompetens', 'service', 'största', 'kommun', 'ansvar', 'försäljning', 'vikt', 'anställda', 'utveckla', 'sveriges', 'består', 'intresse', 'stort', 
#     'idag', 'behov', 'få', 'tal', 'säljare', 'välkommen', 'möjlighet', 'positiv', 'ligger', 'såväl', 'ta', 'verksamhet', 'två', 'viktigt', 'verksamheten', 'elever', 'jobba', 'minst', 'to', 'of', 
#     'egen', 'rätt', 'skapa', 'företaget', 'inriktning', 'ge', 'skrift', 'lärare', 'hög', 'människor', 'stora', 'tjänster', 'skola', 'nära', 'egna', 'sökande', 'möjligheter', 'produkter', 'tycker', 
#     'rekrytering', 'annan', 'liknande', 'stöd', 'hemsida', 'krävs', 'samarbetsförmåga', 'tre', 'annat','erbjuda', 'löpande', 'senast', 'väl', 'göteborg', 'ansvarar', 'se', 'övriga', 'arbetsuppgifterna', 
#     'skolan', 'flera', 'anställning', 'heltid', 'tar', 'ger', 'arbetsplatsuppgifter', 'omgående', 'samarbeta', 'cirka', 'arbetat', 'utifrån', 'ansvara', 'motsvarande', 'noggrann', 'arbets', 'bakgrund']



## Tokenization, stemming and stopword removal
def preprocess_swedish_text(text):
    tokens = word_tokenize(str(text), language='swedish')  # Convert to string. This caused errors previously
    # stop_words = set(stopwords.words('swedish') + manual_stopwords)   # Manual stopwords added here
    stop_words = set(stopwords.words('swedish'))                        # Without manual stopwords added here
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    stemmer = SnowballStemmer('swedish')
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    # return (stemmed_tokens)            ## TWO VARIANTS here
    return ' '.join(stemmed_tokens)     ## This one removes quotes (' ') from description. Reduces filesize a bit in the end

# # # use this if you want to apply preprocessing function to "description.text" column and write to new column
# data['preprocessed_text'] = data['description.text'].apply(preprocess_swedish_text)

# # # use this if you want to  REPLACE "description.text" column with the preprocessed text column
data['description'] = data['description'].apply(preprocess_swedish_text)  ## verkar vara olika i olika dataset

# # # Write preprocessed data to a new CSV file
data.to_csv("preprocessed_data_4.csv", index=False)
