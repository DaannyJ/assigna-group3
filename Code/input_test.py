import pandas as pd
from collections import Counter
from preprocessor import preprocess_swedish_text
from excluded_words_list import * 

# Read the text file into a DataFrame
#df = pd.read_csv('C:/Users/jonat/Documents/GitHub/assigna-group3/Code/text_input.txt', sep='\t', header=None, names=['description'], encoding='utf-8')
df = pd.read_table('C:/Users/jonat/Documents/GitHub/assigna-group3/Code/text_input.txt', header= None, names=['description'], encoding='utf-8')

# Set display option for column width
pd.set_option('display.max_colwidth', None)
print(type(df['description']))
#remove /n
#df['description'] = df['description'].strip() #funkar ej
df['description'] = df['description'].str.replace(r'\n', '')

print(df['description'])
df['description'] = df['description'].apply(preprocess_swedish_text)
print(type(df))
print(df['description'])
print(df.head)


# # # Format df with ''
# def format_df(df):
#     for _, row in df.iterrows():
#         description = row['description']
#         return description
    
# asdf = (format_df(df))
# print(asdf)
# print(type(asdf))
    
# df_new = pd.DataFrame({'description': [asdf]})
# print(df_new)
# print(type(df_new))


# def get_top_words_and_combinations(df):

#     # Create lists to store all words and combinations
#     all_words = []
#     all_combinations = []

#     # Extract words and combinations from tokenized descriptions
#     for desc in df['description']:
#         words = re.findall(r'\w+', desc.lower())
#         all_words.extend(words)
#         combinations = list(ngrams(words, 2))
#         all_combinations.extend(combinations)

#     # Excluded words and combinations are stored within functions in separate files
#     # These are stored in excluded_words_list.py
#     excluded_words = excluded_monograms()
#     excluded_combinations = excluded_bigrams()

#     all_words = [word for word in all_words if word not in excluded_words]
#     all_combinations = [combination for combination in all_combinations if combination not in excluded_combinations]


#     return all_words, all_combinations


# words, combinations = get_top_words_and_combinations(df)

# print(words, combinations)


































# def excluder(data_frame):
#     # Extract words and combinations from tokenized descriptions
#     for desc in data_frame['description']:
#         words = re.findall(r'\w+', desc.lower())
#         all_words.extend(words)
#         combinations = list(ngrams(words, 2))
#         all_combinations.extend(combinations)

#     all_words = []
#     all_combinations = []

#     # Get files
#     excluded_words = excluded_monograms()
#     excluded_combinations = excluded_bigrams()

#     # Exclude words and word combos
#     all_words = [word for word in all_words if word not in excluded_words]
#     all_combinations = [combination for combination in all_combinations if combination not in excluded_combinations]


#     return all_words, all_combinations


# df = (excluder(df))
# print("\n \n \n")
# print(df)