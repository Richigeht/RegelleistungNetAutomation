import pandas as pd
import requests
from datetime import datetime
import os

# Define the current date
current_date = datetime.now().strftime('%Y-%m-%d')

# Create the results_xlsx folder if it doesn't exist
results_folder = 'results_xlsx'
os.makedirs(results_folder, exist_ok=True)

# Define the URL with placeholders for date
base_url = "https://www.regelleistung.net/apps/cpp-publisher/api/v1/download/tenders/anonymousresults?date={}&exportFormat=xlsx&market=CAPACITY&productTypes=mFRR"

# Build the full URL with the current date
url = base_url.format(current_date)

# Define the output filename with the current date
output_filename = f"{current_date}_results.xlsx"

try:
    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Save the content to a file in the results folder
        with open(os.path.join(results_folder, output_filename), 'wb') as file:
            file.write(response.content)

        print(f'File downloaded and saved as {output_filename} in {results_folder}')

    else:
        print(f'File download failed. Status code: {response.status_code}')

except Exception as e:
    print(f'An error occurred during the download: {str(e)}')

# Create the input XLSX filename based on the current date
input_xlsx_file = os.path.join(results_folder, output_filename)
output_csv_file = 'output.csv'

try:
    # Read the downloaded XLSX file into a DataFrame
    df = pd.read_excel(input_xlsx_file)

    # Save the DataFrame as a CSV file
    df.to_csv(output_csv_file, index=False)

    print(f'XLSX to CSV conversion successful. CSV file saved as {output_csv_file}')

except Exception as e:
    print(f'XLSX to CSV conversion error: {str(e)}')
