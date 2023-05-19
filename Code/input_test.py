import pandas as pd
from collections import Counter
from preprocessor import preprocess_swedish_text
from excluded_words_list import * 

# Read the text file as a single string
with open('C:/Users/carlt/Documents/TIG326/kod till projektet/assigna-group3/code/text_input.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Create a DataFrame with a single column
df = pd.DataFrame({'description': [content]})
pd.set_option('display.max_colwidth', None)

# Print the DataFrame
df['description'] = df['description'].apply(preprocess_swedish_text)

print(df)

def excluder(df_col):


    # Excluded monograms
    excluded_monos = excluded_monograms()
    description_filtered = [word for word in df_col if word not in excluded_monos]

    # Excluded bigrams
    excluded_bis = excluded_bigrams()
    description_filtered = [description_filtered[i] for i in range(len(description_filtered)-1) if (description_filtered[i], description_filtered[i+1]) not in excluded_bis]

    return description_filtered


print("👃"*70)
print(excluder(df['description']))