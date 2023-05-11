import pandas as pd
import json

# assuming your JSON file is named "2006.json"
with open('json_files/YEAR.json') as f:
    data = json.load(f)

# flatten the JSON data into a dataframe
df1 = pd.json_normalize(data)

df1.to_csv("YEAR.csv")
