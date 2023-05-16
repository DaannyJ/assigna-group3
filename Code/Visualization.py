import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def visualize_data(df):
    # Read the CSV file into a pandas DataFrame
   

    # Calculate the number of job ads (rows)
    num_rows = len(df)

    # Calculate the length of each ad description
    desc_len = df['description.text'].str.len()  ### WARNING! Description.text or not

    # Calculate the average word length
    word_lengths = df['description.text'].str.split().apply(lambda x: [len(w) for w in x])
    avg_word_length = np.mean([item for sublist in word_lengths for item in sublist])

    # Calculate the median word length
    median_word_length = np.median([item for sublist in word_lengths for item in sublist])

    # Create a bar chart to display the number of job ads, description length, average word length, and median word length
    metrics = ['Number of Job Ads', 'Description Length', 'Average Word Length', 'Median Word Length']
    values = [num_rows, desc_len.mean(), avg_word_length, median_word_length]

    plt.figure(figsize=(10, 6))
    plt.bar(metrics, values)

    # Add data labels to the bars
    for i, value in enumerate(values):
        plt.text(i, value, str(round(value, 2)), ha='center', va='bottom')


    # Add labels and title to the chart
    plt.xlabel('Metrics')
    plt.ylabel('Value')
    plt.title('Job Ad Data Analysis')

    # Display the chart
    plt.show()

    

