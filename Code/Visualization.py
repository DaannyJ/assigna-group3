import pandas as pd
import matplotlib.pyplot as plt
def visualize_data(csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Calculate the number of job ads (rows)
    num_rows = len(df)

    # Calculate the length of each ad description
    df['description_length'] = df['description'].str.len()

    # Create a bar chart to display the number of job ads and description length
    plt.figure(figsize=(8, 6))  # Adjust the figure size as per your preference
    plt.bar(['Number of Job Ads', 'Description Length'], [num_rows, df['description_length'].mean()])

    # Add data labels to the bars
    for i, value in enumerate([num_rows, df['description_length'].mean()]):
        plt.text(i, value, str(value), ha='center', va='bottom')

    # Add labels and title to the chart
    plt.xlabel('Metrics')
    plt.ylabel('Value')
    plt.title('Job Ad Data Analysis')

    # Display the chart
    plt.show()

