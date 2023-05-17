import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Set up the header and description
st.title("Buzzwords Analysis")
st.sidebar.markdown("""
    ## Description
    Our tool is a buzzword checker designed to help companies improve their job ads. The tool utilizes a cosine similarity algorithm to compare the text of a job ad to a pre-defined list of industry-specific buzzwords and phrases. The tool identifies the presence of these buzzwords and assigns a score to the job ad based on how many buzzwords are included.

    This tool is invaluable for companies who want to ensure their job ads are attractive to top talent in their industry. By including the right buzzwords and phrases in their job ads, companies can make sure their job postings stand out and attract the right candidates.
""")


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
        job_ad_text = uploaded_file.read()
    else:
        st.warning("Please upload a file or enter text.")

# Define the list of job titles
job_titles = [
    'Undersköterskor, hemtjänst, hemsjukvård och äldreboende',
    'Grundskollärare',
    'Butikssäljare, fackhandel',
    'Lager- och terminalpersonal',
    'Mjukvaru- och systemutvecklare m.fl.',
    'Barnskötare',
    'Butikssäljare, dagligvaror',
    'Företagssäljare',
    'Vårdbiträden',
    'Städare',
    'Vårdare, boendestödjare',
    'Övriga kontorsassistenter och sekreterare',
    'Personliga assistenter',
    'Förskollärare',
    'Restaurang- och köksbiträden m.fl.',
    'Planerare och utredare m.fl.',
    'Lastbilsförare m.fl.',
    'Grundutbildade sjuksköterskor',
    'Maskinställare och maskinoperatörer, metallarbete',
    'Träarbetare, snickare m.fl.',
    'Fastighetsskötare',
    'Elevassistenter m.fl.',
    'Lednings- och organisationsutvecklare',
    'Kockar och kallskänkor',
    'Undersköterskor, vård- och specialavdelning',
    'Ekonomiassistenter m.fl.',
    'Installations- och serviceelektriker',
    'Kundtjänstpersonal',
    'Motorfordonsmekaniker och fordonsreparatörer',
    'Ingenjörer och tekniker inom elektroteknik'
]
#s
# Define the search function
def search_job_titles(query):
    matches = [title for title in job_titles if query.lower() in title.lower()]
    return matches

# Search for job titles based on user input
search_query = st.sidebar.text_input("Search Job Titles")
search_results = search_job_titles(search_query)

# Display the search results
st.sidebar.markdown("### Search Results")
for result in search_results:
    st.sidebar.write(result)

# Calculate the similarity score and buzzword count
if job_ad_text:
    similarity_score = get_cosine_similarity_score(job_ad_text, ' '.join(buzzwords))
    buzzword_count = sum([1 for word in buzzwords if word in job_ad_text.lower()])
else:
    similarity_score = 0
    buzzword_count = 0

# Display the results
st.markdown(f"### Results for {industry}")
st.write(f"Cosine Similarity Score: {similarity_score:.2f}")
st.write(f"Buzzword Count: {buzzword_count}")
