import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Set up the header and description
st.title("Buzzwords Analysis")
st.sidebar.markdown("""
    ## Description
    Our tool is a buzzword checker designed to help companies improve their job ads. The tool utilizes a cosine similarity algorithm to compare the text of a job ad to a pre-defined list of industry-specific buzzwords and phrases. The tool identifies the presence of these buzzwords and assigns a score to the job ad based on how many buzzwords are included.

    This tool is invaluable for companies who want to ensure their job ads are attractive to top talent in their industry. By including the right buzzwords and phrases in their job ads, companies can make sure their job postings stand out and attract the right candidates.
""")

# Define the industry filter
industry = st.sidebar.selectbox(
    "Industry",
    ("Private Sector", "Public Sector")
)
#Hej
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

# Define the function to search for matches in the list
def search_keywords(keyword):
    matches = []
    for item in data:
        if keyword.lower() in item[0].lower():
            matches.append(item[0])
    return matches

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

search_input = st.text_input("Search for a job title")

# Define the list of buzzwords and phrases
data = [
    ['Undersköterskor, hemtjänst, hemsjukvård och äldreboende'],
    ['Grundskollärare'],
    ['Butikssäljare, fackhandel'],
    ['Lager- och terminalpersonal'],
    ['Mjukvaru- och systemutvecklare m.fl.'],
    ['Barnskötare'],
    ['Butikssäljare, dagligvaror'],
    ['Företagssäljare'],
    ['Vårdbiträden'],
    ['Städare'],
    ['Vårdare, boendestödjare'],
    ['Övriga kontorsassistenter och sekreterare'],
    ['Personliga assistenter'],
    ['Förskollärare'],
    ['Restaurang- och köksbiträden m.fl.'],
    ['Planerare och utredare m.fl.'],
    ['Lastbilsförare m.fl.'],
    ['Grundutbildade sjuksköterskor'],
    ['Maskinställare och maskinoperatörer, metallarbete'],
    ['Träarbetare, snickare m.fl.'],
    ['Fastighetsskötare'],
    ['Elevassistenter m.fl.'],
    ['Lednings- och organisationsutvecklare'],
    ['Kockar och kallskänkor'],
    ['Undersköterskor, vård- och specialavdelning'],
    ['Ekonomiassistenter m.fl.'],
    ['Installations- och serviceelektriker'],
    ['Kundtjänstpersonal'],
    ['Motorfordonsmekaniker och fordonsreparatörer'],
    ['Ingenjörer och tekniker inom elektroteknik']
]

# Calculate the similarity score and buzzword count
if job_ad_text:
    similarity_score = get_cosine_similarity_score(job_ad_text, ' '.join([item[0] for item in data]))
    buzzword_count = sum([1 for word in [item[0].lower() for item in data] if word in job_ad_text.lower()])
else:
    similarity_score = 0
    buzzword_count = 0

# Search for matches in the list
if search_input:
    search_results = search_keywords(search_input)
else:
    search_results = []

# Display the search results
st.markdown("### Search Results")
if search_results:
    for result in search_results:
        st.write(result)
else:
    st.write("No matching results found.")

# Display the results
st.markdown(f"### Results for {industry}")
st.write(f"Cosine Similarity Score: {similarity_score:.2f}")
st.write(f"Buzzword Count: {buzzword_count}")
