import streamlit as st ####   för att köra stremalit testa att köra detta i cmd: python -m streamlit run streamlit_app.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.util import ngrams
import re
import altair as alt
from preprocessor import *
from cosine_1 import get_buzz

# Set up the header and description
st.title("Buzzwords Analysis")
st.sidebar.markdown(
    """
    ## Description
    iahiashaidsidaiho hiodashiodshioda
    """
)

def buzz_monograms():
    return [
        'driv',
        'team',
        'självständ',
        'fokus']

def buzz_bigrams():
    return [
        ('person', 'egenskap'),
        ('gör', 'skilln'),
('god', 'samarbetsförmåg'),
('högt', 'tempo')]



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
    buzzwords_bi = buzz_bigrams()
    all_words = re.findall(r'\w+', pp_input_text.lower())
    # Filter words and keep only the ones that are present in buzzwords_mono. 
    monograms = [word for word in all_words if word in buzzwords_mono]
    
    all_bigrams = list(ngrams(all_words, 2))

    bigrams = [bigram for bigram in all_bigrams if bigram in buzzwords_bi]

    # join the input text with buzzwords list and calculate the cosine similarity score
    similarity_score_mono = get_cosine_similarity_score(pp_input_text, ' '.join(buzzwords_mono))
    similarity_score_bi = get_cosine_similarity_score(pp_input_text, ' '.join([' '.join(bigram) for bigram in bigrams]))

    #vectorizer_bigrams = TfidfVectorizer(pp_input_text=bigrams, ngram_range=(2, 2))

    buzzword_count_mono = len(monograms)
    buzzword_count_bi = len(bigrams)

else:
    similarity_score_mono = 0
    similarity_score_bi = 0
    buzzword_count_mono = 0
    buzzword_count_bi = 0



# Define the color thresholds
high_threshold = 0.8
low_threshold = 0.5

# Format the similarity scores dynamically based on their values
score_color_mono = ""
if similarity_score_mono > high_threshold:
    score_color_mono = "red"
elif similarity_score_mono < low_threshold:
    score_color_mono = "green"
else:
    score_color_mono = "orange"

score_color_bi = ""
if similarity_score_bi > high_threshold:
    score_color_bi = "red"
elif similarity_score_bi < low_threshold:
    score_color_bi = "green"
else:
    score_color_bi = "orange"

# Display the results
st.markdown("### Results")
st.markdown(f"Monogram Cosine Similarity Score: <span style='color:{score_color_mono};'>{similarity_score_mono:.2f}</span>", unsafe_allow_html=True)
st.write(f"Monogram Buzzword Count: {buzzword_count_mono}")

st.markdown(f"Bigram Cosine Similarity Score: <span style='color:{score_color_bi};'>{similarity_score_bi:.2f}</span>", unsafe_allow_html=True)
st.write(f"Bigram Buzzword Count: {buzzword_count_bi}")

# Histogram chart
st.markdown("### Histogram Chart")

# List of values
values = get_buzz()

# Create a DataFrame for the histogram chart
df_histogram = pd.DataFrame({'Value': values})

bin_size = 0.007
highlight_value = 0.18 # ###########################################3#################3
bin_max = df_histogram['Value'].max()

# Create the histogram chart with explicit bin transform
histogram_chart = alt.Chart(df_histogram).transform_bin(
    "binned_value", "Value", bin=alt.Bin(maxbins=int(bin_max / bin_size))
).mark_bar().encode(
    x=alt.X('binned_value:Q', title='Value Bins'),
    y='count()',
    color=alt.condition(
        alt.datum.binned_value == highlight_value,
        alt.value('red'),  # Color for the highlighted bin
        alt.value('lightblue')  # Color for other bins
    ),
    tooltip='count()'
).add_selection(
    alt.selection_single(fields=['binned_value'], init={'binned_value': highlight_value})
)
# Display the histogram chart
histogram_chart
'''
# Plot the histogram using Altair
histogram_chart = alt.Chart(df_histogram).mark_bar().encode(
    alt.X('Value', bin=alt.Bin(step=0.007)),  # Specify the bin width
    y='count()',
    color=alt.value('lightblue')
).properties(
    width=700,
    height=400
)

'''
# Add red dots for the similarity scores
# dot_chart_mono = alt.Chart(pd.DataFrame({'Value': [similarity_score_mono]})).mark_point(color='red', size=100).encode(
#     x='Value',
#     y='count()'
# )

# dot_chart_bi = alt.Chart(pd.DataFrame({'Value': [similarity_score_bi]})).mark_point(color='red', size=100).encode(
#     x='Value',
#     y='count()'
# )

# # Layer the histogram and the dot charts
# layered_chart = histogram_chart + dot_chart_mono + dot_chart_bi

# st.altair_chart(layered_chart)

st.altair_chart(histogram_chart)
# Export DataFrame to another file (e.g., CSV)
df.to_csv("job_ad_data.csv", index=False)
