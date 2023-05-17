import pandas as pd
import nltk

from Visualization import * # EDA for the preprocessing
from language_remover import language_remover # For removing non swedish ads
from preprocessor import preprocess_swedish_text # removes special characters and numbers, tokenizes, stems, and removes stopwords

## Load you CSV. Pay attention to if your CSV has "description.text" or "description". Change code accordingly
data = pd.read_csv('C:/Users/carlt/Documents/TIG326/kod till projektet/datasets/sample_1000_per_year.csv', index_col=0)

# visualize data about your texts before processing. Takes a dataframe
visualize_data(data)

# Run language_remover. Also takes a dataframe. Specify which column you want to work with in the language_remover file
swedish_ads = language_remover(data)

# Runs the preprocessor. REPLACES the "description.text" (or sometimes "description") column with the preprocessed text column
swedish_ads['description'] = swedish_ads['description'].apply(preprocess_swedish_text)    

# Visualize data about texts again, but after processing. Remember that the dataframe has changed names
visualize_data(swedish_ads)

print(swedish_ads)


# # # Write preprocessed data to a new CSV file
data.to_csv("preprocessed_swe_1.csv", index=False)

# # # exploratory crap
# pd.set_option('display.max_colwidth', 120)
# df = pd.DataFrame(swedish_ads.description)
# print(df.head(20))