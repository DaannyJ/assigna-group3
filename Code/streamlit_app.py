import streamlit as st
import pandas as pd

# Add the header
st.header("Buzzwords analysis")

# Add file uploader and text input
data_file = st.file_uploader("Upload a file", type=["txt"])
text_input = st.text_input("Enter text to analyze")

# Define the buzzwords to search for
buzzwords = ["du", "nej", "hej"]

# Define function to analyze text
def analyze_text(text):
    # Convert text to lowercase for case-insensitive matching
    text = text.lower()
    
    # Count occurrences of each buzzword in the text
    counts = {buzzword: text.count(buzzword) for buzzword in buzzwords}
    
    # Create a DataFrame to store the results
    df = pd.DataFrame.from_dict(counts, orient='index', columns=['count'])
    
    return df

# Analyze data based on user input
if data_file is not None:
    # Read data from the uploaded file
    data = data_file.read().decode("utf-8")
    
    # Analyze the data and display the results
    result = analyze_text(data)
    st.write(result)
elif text_input != "":
    # Analyze the text and display the results
    result = analyze_text(text_input)
    st.write(result)
