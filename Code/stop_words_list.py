import pandas as pd

def remove_custom_words(df, custom_words=None):
    if custom_words is None:
        
        custom_words = ['word1', 'word2','word3']  # Default list of custom words to remove

    # Filter words for each row in the "description" column
    df["description"] = df["description"].apply(lambda x: [word for word in x if word.lower() not in custom_words])

    return df
'''
# Example:
# Load the dataset into a pandas DataFrame
df = pd.read_csv('file.csv')
# Call the function without providing custom_words parameter
df_without_custom_words = remove_custom_words(df)
# Print the modified DataFrame
print(df_without_custom_words)
'''




#GAMLA
'''
import nltk
from nltk.corpus import stopwords

swedish_stopwords = stopwords.words('swedish')
english_stopwords = stopwords.words('english')


exclude_words = [
    'och', 'och/eller', 'tjänst', 'hemtjänst', 'skicka', 'kund', 'verksamma',
    'bil', 'deltid', 'barnen', 'täby', 'hsb', 'telefon', 'hand', 'hjälpa',
    'henån', 'for', 'omsorg', 'familjen', 'vikariat', 'emot', 'medan',
    'perfekta','söker', 'sker', 'måste', 'all', 'bör', 'kommer',
    'i', 'du', 'har', 'din', 'själv', 'det', '-', 'vi',
    'av', 'på', 'inte', 'men', 'kan', 'om', 'eller',
    'när', 'utan', 'vid', 'alla', 'blir', 'mot', 'mycket', 'nu',
    'än', 'andra', 'bara', 'bli', 'både', 'där', 'dessa', 'dock',
    'genom', 'ha', 'hade', 'han', 'hans', 'hos', 'hur', 'in', 'inga', 'inom',
    'inuti', 'ja', 'jag', 'ju', 't.ex.', 'bl.a.', 'd.v.s', 'enligt',
    'mellan', 'ofta', 'ibland', 'många', 'behöva', 'också', 'även', 'dessutom',
    'ytterligare', 'för det första', 'för det andra', 'tilläggas', 'slutligen',
    'sist men inte minst', 'inledningsvis', 'omedelbart därefter', 'under tiden',
    'samtidigt', 'efter', 'så småningom', 'efter ett tag', 'först', 'senare',
    'tidigare', 'till sist', 'dels-dels', 'jämfört med', 'såsom',
    'på samma sätt som', 'på så sätt', 'i likhet med', 'en likartad uppfattning',
    'likartat', 'i sin tur', 'fördelarna', 'nackdelarna', 'däremot',
    'men emellertid', 'ändå', 'icke desto mindre', 'trots', 'trots allt',
    'trots att', 'även om', 'i motsats till', 'å ena sidan', 'å andra sidan',
    'när allt kommer omkring', 'en skillnad är', 'tvärtemot', 'tvärtom',
    'i gengäld', 'till exempel', 'exempelvis', 'bland annat',
    'det vill säga', 'illustrerar', 'illustreras', 'som ett exempel på', 'belyser',
    'visar', 'här urskiljer sig', 'närmare bestämt', 'särskilt', 'i synnerhet', 
    'som', 'därför', 'således', 'detta beror på', 'alltså', 'på grund av', 
    'av detta skäl', 'beroende på', 'orsaken är', 'mot den bakgrunden', 
    'anledningen är', 'målet är att', 'detta går ut på att', 'i syfte att', 
    'som en följd av', 'härav följer', 'följaktligen', 'sålunda', 'resultatet blir', 
    'slutsatsen blir', 'vilket leder till', 'det(ta) beror på', 'att',
    'en', 'hon', 'den', 'med', 'var', 'sig', 'för', 
    'så', 'till', 'är', 'ett', 'de', 'icke', 'mig',
    'henne', 'då', 'sin', 'honom', 'skulle', 'hennes',
    'min', 'man', 'ej', 'kunde', 'något', 'från', 'ut', 'upp', 
    'dem', 'vara', 'vad', 'över', 'dig', 'sina', 'här', 
    'under', 'någon', 'allt', 'sedan', 'denna', 
    'detta', 'åt', 'varit', 'ingen', 'mitt', 'ni', 'blev', 'oss',
    'några', 'deras', 'mina', 'samma', 'vilken', 'er', 'sådan', 'vår', 
    'blivit', 'dess', 'sådant', 'varför', 'varje', 'vilka', 'ditt', 
    'vem', 'vilket', 'sitta', 'sådana', 'vart', 'dina', 'vars', 'vårt', 'våra', 'ert', 
    'era', 'vilkas', 'samt', 'erfarenhet', 'arbeta', 'vill', 'arbetsuppgifter', 'arbete',
    'arbetar', 'gärna', 'ska', 'god', 'ansökan', 'finns', 'utbildning', 'ser', 'person',
    'ca', 'arbetet', 'tjänsten', 'skall', 'goda', 'olika', 'företag', 'ab', 'år', 'ingår', 
    'kunder', 'stor', 'medarbetare', 'erbjuder', 'kvalifikationer', 'krav', 'kunna', 'and', 
    'nya', 'kunskaper', 'förmåga', 'innebär', 'personal', 'bra', 'behöver', 'sverige', 'via', 
    'mer', 'års', 'the', 'personer', 'barn', 'hela', 'självständigt', 'tillsammans', 
    'stockholm', 'del', 'uppdrag', 'får', 'kompetens', 'service', 'största', 'kommun', 'ansvar', 
    'försäljning', 'vikt', 'anställda', 'utveckla', 'sveriges', 'består', 'intresse', 'stort', 
    'idag', 'behov', 'få', 'tal', 'säljare', 'välkommen', 'möjlighet', 'positiv', 'ligger', 'såväl', 
    'ta', 'verksamhet', 'två', 'viktigt', 'verksamheten', 'elever', 'jobba', 'minst', 'to', 'of', 
    'egen', 'rätt', 'skapa', 'företaget', 'inriktning', 'ge', 'skrift', 'lärare', 'hög', 'människor', 
    'stora', 'tjänster', 'skola', 'nära', 'egna', 'sökande', 'möjligheter', 'produkter', 'tycker', 
    'rekrytering', 'annan', 'liknande', 'stöd', 'hemsida', 'krävs', 'samarbetsförmåga', 'tre', 'annat',
    'erbjuda', 'löpande', 'senast', 'väl', 'göteborg', 'ansvarar', 'se', 'övriga', 'arbetsuppgifterna', 
    'skolan', 'flera', 'anställning', 'heltid', 'tar', 'ger', 'arbetsplatsuppgifter', 'omgående', 
    'samarbeta', 'cirka', 'arbetat', 'utifrån', 'ansvara', 'motsvarande', 'noggrann', 'arbets', 'bakgrund']

swedish_stopwords += exclude_words
swedish_stopwords += english_stopwords
'''



#NYA BLYAT
stopwords_list = [
    'arbet',
    'kund',
    'sök',
    'hos',
    'tjänst',
    'topwork',
    'komm',
    'medarbet',
    'person',
    'nya',
    'erfaren',
    'god',
    'rätt',
    'utveckl',
    'roll',
    'anställning',
    'vill',
    'ska',
    'får',
    'vikt',
    'jobb',
    'samt',
    'båd',
    'finn',
    'krav',
    'företag',
    'kunskap',
    'svensk',
    'utmaning',
    'tid',
    'möj',
    'mål',
    'uppdrag',
    'stor',
    'hitt',
    'körkort',
    'rekrytering',
    'trygg',
    'bygg',
    'erbjud',
    'även',
    'b',
    'in',
    'konsult',
    'stött',
    'sen',
    'del',
    'oavset',
    'arbetsuppgift',
    'meriter'
]
