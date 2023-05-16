import pandas as pd

# Read in the CSV file
df = pd.read_csv('DIN FILEPATH HÄR')

# Select only the desired columns
df = df[['headline','publication_date', 'description.text']]


# drop all rows where there are null and nan
df = df.dropna()
print(df.head)

# skriver till ny csv fil
df.to_csv("FILNAMN.csv")
