from collections import Counter
from nltk import ngrams
import pandas as pd
import re

data = pd.read_csv('C:/Users/danie/Documents/assigna-group3/Code/preprocessed_swe_1.csv')

def get_top_words_and_combinations(df, row_limit, num_words, num_combinations):
    # Limit the DataFrame to the specified number of rows
    df = df.head(row_limit)

    # Create lists to store all words and combinations
    all_words = []
    all_combinations = []

    # Extract words and combinations from tokenized descriptions
    for desc in df['description']:
        words = re.findall(r'\w+', desc.lower())
        all_words.extend(words)
        combinations = list(ngrams(words, 2))
        all_combinations.extend(combinations)

    # Excluded words and combinations
    excluded_words = [
        'sök',
        'komm',
        'person',
        'samt',
        'tjänst',
        'erfaren',
        'kund',
        'god',
        'vill',
        'hos',
        'möj',
        'jobb',
        'erbjud',
        'ansökan',
        'vikt',
        'roll',
        'utveckl',
        'även',
        'ser',
        'båd',
        'medarbet',
        'arbetsuppgift',
        'del',
        'gör',
        'ska',
        'se',
        'finn',
        'verksam',
        'får',
        'stor',
        'olik',
        'svensk',
        'dag',
        'tid',
        'kunskap',
        'gärn',
        'utbildning',
        'skap',
        'mer',
        'sver',
        'in',
        'arbetet',
        'andr',
        'driv',
        'meriter',
        'hjälp',
        'löp',
        'nya',
        'genom',
        'välkomm',
        'samarbet',
        'uppdrag',
        'led',
        'bra',
        'ta',
        'kolleg',
        'behöv',
        'utveckling',
        'team',
        'innebär',
        'hel',
        'krav',
        'också',
        'enl',
        'kontak',
        'tal',
        'därför',
        'företag',
        'via',
        'www',
        'trygg',
        'kunn',
        'förmåg',
        'ansvar',
        'servic',
        'sätt',
        'triv',
        'kommun',
        'idag',
        'fler',
        'rätt',
        'bäst',
        'övr',
        'företaget',
        'behov',
        'barn',
        'få',
        'rekrytering',
        'ansv',
        'människ',
        'anställning',
        'tar',
        'skrift',
        'stort',
        'bidr',
        'hög',
        'sker',
        'lär',
        'när',
        'anställd'

    ]

    excluded_combinations = [
        ("tal", "skrift"),
        ("välkomm", "ansökan"),
        ("stor", "vikt"),
        ("god", "kunskap"),
        ("ser", "gärn"),
        ("in", "ansökan"),
        ("erfaren", "arbet"),
        ("bland", "ann"),
        ("redan", "idag"),
        ("hos", "kund"),
        ("tid", "erfaren"),
        ("komm", "arbet"),
        ("sker", "löp"),
        ("enl", "överenskomm"),
        ("års", "erfaren"),
        ("varmt", "välkomm"),
        ("skick", "in"),
        ("person", "egenskap"),
        ("b", "körkort"),
        ("läs", "mer"),
        ("svensk", "engelsk"),
        ("vikt", "person"),
        ("https", "www"),
        ("lägg", "stor"),
        ("sök", "tjänst"),
        ("sist", "ansökningsdag"),
        ("vill", "arbet"),
        ("gör", "skilln"),
        ("tjänst", "komm"),
        ("person", "lämp"),
        ("båd", "tal"),
        ("arbet", "självständ"),
        ("ansökan", "redan"),
        ("kunskap", "svensk"),
        ("fram", "emot"),
        ("ser", "fram"),
        ("sök", "vill"),
        ("komm", "tillsät"),
        ("tillsät", "innan"),
        ("jobb", "hos"),
        ("när", "samarbet"),
        ("meriter", "erfaren"),
        ("kvalifikation", "sök"),
        ("innan", "sist"),
        ("hos", "får"),
        ("god", "förmåg"),
        ("hälso", "sjukvård"),
        ("person", "brev"),
        ("god", "samarbetsförmåg"),
        ("snart", "möj"),
        ("högt", "tempo"),
        ("löp", "tjänst"),
        ("vill", "jobb"),
        ("rätt", "person"),
        ("får", "möj"),
        ("person", "assistent"),
        ("lyck", "roll"),
        ("arbet", "tillsamman"),
        ("svensk", "språket"),
        ("sver", "störst"),
        ("vikt", "del"),
        ("emot", "ansökning"),
        ("intervju", "sker"),
        ("möj", "arbet"),
        ("löp", "urval"),
        ("urval", "intervju"),
        ("ansökning", "via"),
        ("känn", "trygg"),
        ("behärsk", "svensk"),
        ("bemanning", "rekryteringsföretag"),
        ("vill", "utveckl"),
        ("möj", "utveckl"),
        ("svensk", "tal"),
        ("mer", "information"),
        ("utdrag", "ur"),
        ("stor", "möj"),
        ("emot", "ansökan"),
        ("t", "ex"),
        ("komm", "få"),
        ("ska", "kunn"),
        ("allakando", "läxhjälp"),
        ("god", "möj"),
        ("komm", "ske"),
        ("inget", "krav"),
        ("vet", "mer"),
        ("lägg", "person"),
        ("tillsamman", "kolleg"),
        ("tar", "emot"),
        ("komm", "även"),
        ("anställning", "hos"),
        ("uppsat", "mål"),
        ("eget", "ansv"),
        ("hel", "sver"),
        ("arbetsuppgift", "komm"),
        ("västr", "götalandsregion"),
        ("urval", "sker"),
        ("triv", "arbet"),
        ("minst", "års"),
        ("start", "omgåend"),
        ("arbet", "hos")
    ]


    # Remove excluded words and combinations
    all_words = [word for word in all_words if word not in excluded_words]
    all_combinations = [combination for combination in all_combinations if combination not in excluded_combinations]

    # Count the occurrences of each word and combination
    word_counts = Counter(all_words)
    combination_counts = Counter(all_combinations)

    # Get the most common words and combinations
    top_words = word_counts.most_common(num_words)
    top_combinations = combination_counts.most_common(num_combinations)

    return top_words, top_combinations


top_words, top_combinations = get_top_words_and_combinations(data, 10000, 100, 100)
print("Most common words:")
for word, count in top_words:
    print(f"{word}")

print()

print("Most common two-word combinations:")
for combination, count in top_combinations:
    print(f"{' '.join(combination)}")
