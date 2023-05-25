import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import altair as alt
from preprocessor import *
from cosine_1 import get_buzz
from buzz_words_list import buzz_monograms

# Set up the header and description
st.title("Buzzwords Analysis 🏄‍♂️")
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
    corpus = [str(p) for p in corpus] # this is bad code. Evil. But necessary.
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    similarity_scores = cosine_similarity(X)
    return similarity_scores[0][1]

# Define the main content area
st.markdown("### Enter Job Ad Text")
job_ad_text = st.text_area("Paste your job ad text here")
print(type(job_ad_text))

# Convert input text to DataFrame
df = pd.DataFrame({"job_ad_text": [job_ad_text]})
df['job_ad_text'] = df['job_ad_text'].apply(preprocess_swedish_text)
# Other necessary conversions
asdfasdf = df['job_ad_text'].tolist()
pp_input_text = str(asdfasdf)

# Calculate the similarity score and buzzword count
if job_ad_text:
    buzzwords_mono = buzz_monograms()
    all_words = re.findall(r'\w+', pp_input_text.lower())
    # Filter words and keep only the ones that are present in buzzwords_mono. 
    monograms = [word for word in all_words if word in buzzwords_mono]
    
    # join the input text with buzzwords list and calculate the cosine similarity score
    similarity_score_mono = get_cosine_similarity_score(pp_input_text, ' '.join(buzzwords_mono))

    buzzword_count_mono = len(monograms)

    # Set the highlight_value after calculating the similarity score
    highlight_value = similarity_score_mono

else:
    similarity_score_mono = 0
    buzzword_count_mono = 0
    highlight_value = -1  # Set a value outside the bin range to keep the highlight visible

# Define the color thresholds
high_threshold = 0.8
low_threshold = 0.5

# Format the similarity score dynamically based on its value
score_color_mono = ""
if similarity_score_mono > high_threshold:
    score_color_mono = "red"
elif similarity_score_mono < low_threshold:
    score_color_mono = "green"
else:
    score_color_mono = "orange"

# Display the results
st.markdown("<h3>Results</h3>", unsafe_allow_html=True)
st.markdown(f"<p><strong>Buzz Score (Cosine Similarity):</strong> <span style='color:{score_color_mono}; font-size: 24px;'>{similarity_score_mono:.2f}</span></p>", unsafe_allow_html=True)
st.markdown(f"<p><strong>Buzzword Count:</strong> {buzzword_count_mono}</p>", unsafe_allow_html=True)

# Histogram chart
st.markdown("<h3>Histogram Chart</h3>", unsafe_allow_html=True)

# List of values
values = get_buzz()

# Create a DataFrame for the histogram chart
df_histogram = pd.DataFrame({'Value': values})

bin_size = 0.007
bin_max = df_histogram['Value'].max()

# Create the histogram chart with explicit bin transform
histogram_chart = alt.Chart(df_histogram).transform_bin(
    "binned_value", "Value", bin=alt.Bin(maxbins=int(bin_max / bin_size))
).mark_bar().encode(
    x=alt.X('binned_value:Q', title='Value Bins'),
    y='count()',
    tooltip=['count()', 'binned_value:Q']  # Add tooltips for count and value
).properties(
    width=700,  # Set the width of the histogram chart
    height=400  # Set the height of the histogram chart
)

# Display the histogram chart
st.altair_chart(histogram_chart)

# Export DataFrame to another file (e.g., CSV)
df.to_csv("job_ad_data.csv", index=False)
