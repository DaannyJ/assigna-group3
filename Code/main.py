import pandas as pd
import nltk

from Visualization import * # EDA for the preprocessing
from language_remover import language_remover # For removing non swedish ads
from preprocessor import preprocess_swedish_text

## Load da CSV
data = pd.read_csv('C:/Users/carlt/Documents/TIG326/kod till projektet/datasets/sample_1000_per_year.csv', index_col=0)

# visualize data about your texts before processing
visualize_data(data)

# Run language_remover
swedish_ads = language_remover(data)

# Runs the preprocessor. REPLACES "description.text" column with the preprocessed text column
swedish_ads['description'] = swedish_ads['description'].apply(preprocess_swedish_text)    

# Visualize data about texts again, but after processing
visualize_data(swedish_ads)

print(swedish_ads)


# # # Write preprocessed data to a new CSV file
# data.to_csv("preprocessed_data_15.csv", index=False)

# pd.set_option('display.max_colwidth', 120)
# df = pd.DataFrame(swedish_ads.description)
# print(df.head(20))