import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

    ### At the moment this works with preprocessed data
df = pd.read_csv('C:/Users/carlt/Documents/TIG326/kod till projektet/local_copy/2022_10k_stemmed_headlines_swe.csv')
roles_df = pd.read_csv('C:/Users/carlt/Documents/TIG326/kod till projektet/local_copy/work_roles_3pp+.csv')
pd.set_option('display.max_colwidth', 2)
# print(df['headline'])
# print(roles_df['roles'])

# Merge texts
merged_texts = df['headline'].tolist() + roles_df['roles'].tolist()

# Vectorize the data
vectorizer = TfidfVectorizer(max_df=0.05) # filters out words that are present in more than 10% (0.10) of ads
vectorized_data = vectorizer.fit_transform(merged_texts)

# Split the vectors
headline_vectors = vectorized_data[:len(df)]
role_vectors = vectorized_data[len(df):]

# Calculate cosine similarity
similarity_matrix = cosine_similarity(headline_vectors, role_vectors)

threshold = 0.4 # How close it gotta be to get counted

# Assign the most similar job role based on the threshold
tagged_roles = []
for i in range(len(df)):
    max_similarity = similarity_matrix[i].max()
    if max_similarity >= threshold:
        max_similarity_index = similarity_matrix[i].argmax()
        tagged_role = roles_df['roles'].iloc[max_similarity_index]
    else:
        tagged_role = 'Unknown'  # The ones that can't get tagged get called 'Unknown"
    tagged_roles.append(tagged_role)

df['tagged_role'] = tagged_roles


# # Print the tagged job roles
# print(df[['headline', 'tagged_role']])
print("💻"*50)
# # Show top tags
def print_job_role_counts(df):
    role_counts = df['tagged_role'].value_counts()
    role_counts_df = pd.DataFrame({'Job Role': role_counts.index, 'Count': role_counts.values})
    print(role_counts_df)
print_job_role_counts(df)
print("📡"*50)


# # # # Show only sucessfully tagged roles
tagged_rows = df[df['tagged_role'] != 'Unknown']
print(tagged_rows.shape[0], "rows 🥰✌️")
unknown_rows = df[df['tagged_role'] == 'Unknown']

# Show 100 random
pd.set_option('display.max_rows', None)
random_sample = unknown_rows.sample(n=200, random_state=46)  # sample 100 random
print(random_sample[['headline','tagged_role']])


# row = 2000
# print(df.iloc[row]['headline'], df.iloc[row]['tagged_role'], df.iloc[row]['description'])