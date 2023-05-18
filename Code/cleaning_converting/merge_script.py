import pandas as pd
import glob

# Path to directory containing the CSV files
path = r"C:\Users\danie\Documents\data_convert_to_csv\testing_merge"

# Get a list of all CSV files in the directory
all_files = glob.glob(path + "/*.csv")

# Read each CSV file into a separate DataFrame and store them in a list
dfs = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dfs, axis=0, ignore_index=True)

# Write the merged DataFrame to a new CSV file
merged_df.to_csv("FINAL_merged_csv_files.csv", index=False)
