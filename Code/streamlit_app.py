import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from buzz_words_list import *
from preprocessor import *
import re
import altair as alt
from cosine_1 import *

# Set up the header and description
st.title("Buzzwords Analysis")
st.sidebar.markdown(
    """
    ## Description
    Our tool is a buzzword checker designed to help companies improve their job ads. The tool utilizes a cosine similarity algorithm to compare the text of a job ad to a pre-defined list of industry-specific buzzwords and phrases. The tool identifies the presence of these buzzwords and assigns a score to the job ad based on how many buzzwords are included.

    This tool is invaluable for companies who want to ensure their job ads are attractive to top talent in their industry. By including the right buzzwords and phrases in their job ads, companies can make sure their job postings stand out and attract the right candidates.
    """
)

# Define the function to get the cosine similarity score
def get_cosine_similarity_score(text1, text2):
    corpus = [text1, text2]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    similarity_scores = cosine_similarity(X)
    return similarity_scores[0][1]

# Define the main content area
st.markdown("### Enter Job Ad Text")
job_ad_text = st.text_area("Paste your job ad text here")

# Convert input text to DataFrame
df = pd.DataFrame({"job_ad_text": [job_ad_text]})
df['job_ad_text'] = df['job_ad_text'].apply(preprocess_swedish_text)

# Calculate the similarity score and buzzword count
if job_ad_text:
    buzzwords = get_both()
    similarity_score = get_cosine_similarity_score(job_ad_text, ' '.join(buzzwords))
    buzzword_count = sum([1 for word in buzzwords if re.search(rf'\b{word}\b', job_ad_text.lower())])
else:
    similarity_score = 0
    buzzword_count = 0

# Define the color thresholds
high_threshold = 0.8
low_threshold = 0.5

# Format the similarity score dynamically based on its value
score_color = ""
if similarity_score > high_threshold:
    score_color = "red"
elif similarity_score < low_threshold:
    score_color = "green"
else:
    score_color = "orange"

# Display the results
st.markdown("### Results")
st.markdown(f"Cosine Similarity Score: <span style='color:{score_color};'>{similarity_score:.2f}</span>", unsafe_allow_html=True)
st.write(f"Buzzword Count: {buzzword_count}")

# Histogram chart
st.markdown("### Histogram Chart")

# List of values
values = get_buzz()
values.append(similarity_score)  # Include the similarity score in the values list

# Create a DataFrame for the histogram chart
df_histogram = pd.DataFrame({'Value': values})

# Plot the histogram using Altair
histogram_chart = alt.Chart(df_histogram).mark_bar().encode(
    alt.X('Value', bin=alt.Bin(step=0.007)),  # Specify the bin width
    y='count()',
    color=alt.value('lightblue')
).properties(
    width=700,
    height=400
)

# Add a red dot for the similarity score
dot_chart = alt.Chart(pd.DataFrame({'Value': [similarity_score]})).mark_point(color='red', size=100).encode(
    x='Value',
    y='count()'
)

# Layer the histogram and the dot chart
layered_chart = histogram_chart + dot_chart

st.altair_chart(layered_chart)

# Export DataFrame to another file (e.g., CSV)
df.to_csv("job_ad_data.csv", index=False)
