import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define the header
st.title('Buzzwords Analysis')

# Define the description
st.sidebar.markdown('''
    Our tool is a buzzword checker designed to help companies improve their job ads. 
    The tool utilizes a cosine similarity algorithm to compare the text of a job ad 
    to a pre-defined list of industry-specific buzzwords and phrases. The tool identifies 
    the presence of these buzzwords and assigns a score to the job ad based on how many 
    buzzwords are included. This tool is invaluable for companies who want to ensure their 
    job ads are attractive to top talent in their industry. By including the right buzzwords 
    and phrases in their job ads, companies can make sure their job postings stand out and 
    attract the right candidates. Our buzzword checker is designed to be fast and efficient, 
    allowing companies to check their job ads quickly and easily. With our tool, companies 
    can be confident that their job ads are optimized for maximum impact.
''')

# Define the input options
input_type = st.radio('Select Input Type:', ('Text', 'File'))

# If "Text" is selected, show a text box for input
if input_type == 'Text':
    input_text = st.text_input('Enter Text:')
    # Convert the text input into a list of strings
    input_list = [input_text]

# If "File" is selected, show a file upload button for input
else:
    uploaded_file = st.file_uploader('Upload a File:', type=['txt'])
    # If a file is uploaded, read its contents and convert it into a list of strings
    if uploaded_file is not None:
        input_list = []
        file_contents = uploaded_file.read().decode('utf-8')
        input_list = [file_contents]

# Define the buzzwords
buzzwords = ["du", "nej", "hej"]

# Define the vectorizer and fit it to the buzzwords
vectorizer = CountVectorizer(vocabulary=buzzwords)

# Define a function to calculate the cosine similarity between two texts
def cosine_sim(input_text):
    # Fit the vectorizer to the input text
    X = vectorizer.fit_transform(input_text)
    # Calculate the cosine similarity matrix
    cosine_sim_matrix = cosine_similarity(X)
    return cosine_sim_matrix[0][0]

# Calculate the similarity score and display it
if input_list:
    similarity_score = cosine_sim(input_list)
    st.write('Similarity Score:', similarity_score)
