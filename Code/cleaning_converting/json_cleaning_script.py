import pandas as pd
import json

# Load the JSON data into a pandas DataFrame
with open('json_files/2006.json') as f:
    data = json.load(f)
df = pd.json_normalize(data)

# Select the columns you want to keep
df = df[['headline', 'last_publication_date', 'publication_date',
         'description.conditions', 'description.text',
         'duration.label', 'working_hours_type.label',
         'workplace_address.city', 'workplace_address.municipality_code']]

# Remove rows with NaN/NULL values
df = df.dropna()

# Print the resulting DataFrame
df

df.to_json("2006_cleaned.json") #Updaterar filen