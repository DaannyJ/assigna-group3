import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from buzz_words_list import *

# Set up the header and description
st.set_page_config(page_title="Buzzwords Analysis", page_icon="🔎", layout="wide")
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f7f9fe;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Buzzwords Analysis")
st.sidebar.markdown(
    """
    ## Description
    Our tool is a buzzword checker designed to help companies improve their job ads. The tool utilizes a cosine similarity algorithm to compare the text of a job ad to a pre-defined list of industry-specific buzzwords and phrases. The tool identifies the presence of these buzzwords and assigns a score to the job ad based on how many buzzwords are included.

    This tool is invaluable for companies who want to ensure their job ads are attractive to top talent in their industry. By including the right buzzwords and phrases in their job ads, companies can make sure their job postings stand out and attract the right candidates.
    """
)

# Define the text input or file upload option
option = st.sidebar.radio(
    "Choose an option:",
    ("Input Text", "Upload File")
)

# Define the function to get the cosine similarity score
def get_cosine_similarity_score(text1, text2):
    corpus = [text1, text2]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    similarity_scores = cosine_similarity(X)
    return similarity_scores[0][1]

# Define the main content area
st.markdown("### Enter or Upload Job Ad Text")
if option == "Input Text":
    job_ad_text = st.text_area("Paste your job ad text here")
else:
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Try different encodings until successful decoding
        encodings = ["utf-8", "latin-1", "utf-16"]
        for encoding in encodings:
            try:
                job_ad_text = uploaded_file.read().decode(encoding)
                break
            except UnicodeDecodeError:
                continue
        else:
            st.error("Failed to decode the uploaded file. Please try a different file.")
            job_ad_text = ""
    else:
        job_ad_text = ""

# Calculate the similarity score and buzzword count
if job_ad_text:
    buzzwords = ["INSERT BUZZ WORDS HERE"]
    similarity_score = get_cosine_similarity_score(job_ad_text, ' '.join(buzzwords))
    buzzword_count = sum([1 for word in buzzwords if word in job_ad_text.lower()])
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
