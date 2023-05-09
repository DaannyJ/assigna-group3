import pandas as pd

# Read in the CSV file
df = pd.read_csv("INSERTYEAR_cleaned.csv")

# Select only the desired columns
df_selected = df[['application_deadline', 'headline', 'last_publication_date',
                  'publication_date', 'description.conditions', 'description.text',
                  'duration.label', 'working_hours_type.label',
                  'workplace_address.city', 'workplace_address.municipality_code']]

# Print the new dataframe with only the selected columns
df_selected.to_csv("INSERTYEAR_cleaned_correct.csv")