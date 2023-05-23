import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from buzz_words_list import *
from preprocessor import *
import re
import altair as alt

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
    buzzwords = buzz_monograms()
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

# Scatter chart
st.markdown("### Scatter Chart")

# List of values
values = [0.1394210371349766, 0.1396485613981665, 0.1396485613981665, 0.13794176675022102, 0.13794176675022102, 0.1394210371349766, 0.1396485613981665, 0.13794176675022102, 0.1394210371349766, 0.1394210371349766, 0.13794176675022102, 0.13794176675022102, 0.14187507361030582, 0.13794176675022102, 0.13794176675022102, 0.1394210371349766, 0.1394210371349766, 0.1394210371349766, 0.13794176675022102, 0.13794176675022102, 0.13794176675022102, 0.11242123529636222, 0.18141200201540128, 0.06866887462507401, 0.10837983631416867, 0.1295742117778199, 0.41874458175567536, 0.19246977430465506, 0.16134913775125648, 0.1257701674800333, 0.16251048673044255, 0.11346575675121592]
values.append(similarity_score)  # Include the similarity score in the values list

# Create a DataFrame for the scatter chart
df_scatter = pd.DataFrame({'Index': range(len(values)), 'Value': values})

# Highlight the similarity score
df_scatter['Highlighted'] = [True if val == similarity_score else False for val in values]

# Plot the scatter chart using Altair
highlight_color = alt.condition(
    alt.datum.Highlighted,
    alt.value('red'),
    alt.value('steelblue')
)

scatter_chart = alt.Chart(df_scatter).mark_point(size=100, filled=True).encode(
    x='Index',
    y='Value',
    color=highlight_color
).properties(
    width=600,
    height=400
)

st.altair_chart(scatter_chart)

# Export DataFrame to another file (e.g., CSV)
df.to_csv("job_ad_data.csv", index=False)
