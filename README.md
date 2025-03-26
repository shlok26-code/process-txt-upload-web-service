# Automating Customer Feedback Processing with Python
A script to convert the reviews stored as .txt files and process them into Python dictionaries, then upload the data onto the company’s website (in this project, using Django)


# Processing Text Files with Python and Uploading to a Web Service

## Overview

This project involves processing customer feedback stored as text files and uploading them to a Django-based web service. The script reads the text files, converts them into dictionaries, and then sends them to the web service using HTTP POST requests.

## Features

- Reads customer feedback from `.txt` files.
- Parses the feedback into structured Python dictionaries.
- Uploads the feedback to a Django web service using the `requests` module.
- Provides error handling for failed uploads.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- `requests` module (install using `pip install requests`)
- Access to a running Django web service

## Project Structure

```
├── run.py               # Main script for processing and uploading feedback
├── /data/feedback/      # Directory containing .txt feedback files
├── README.md            # Project documentation
```

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/project-name.git
   cd project-name
   ```
2. Install required dependencies:
   ```sh
   pip install requests
   ```
3. Ensure the Django web service is running and accessible.

## Usage

1. Navigate to the project directory:
   ```sh
   cd project-name
   ```
2. Grant executable permission to the script:
   ```sh
   chmod +x run.py
   ```
3. Run the script:
   ```sh
   ./run.py
   ```

## Code Explanation

```python
#! /usr/bin/env python3

import os  # Importing the os module to interact with the file system
import requests  # Importing requests to send HTTP requests

# Define the base directory where feedback text files are stored
BASEPATH = '/data/feedback/'

# Get a list of all files in the feedback directory
folder = os.listdir(BASEPATH)

# Initialize an empty list to store feedback data
list = []

# Iterate through each file in the feedback directory
for file in folder:
    # Open each file in read mode
    with open(BASEPATH + file, 'r') as f:
        # Read the contents of the file and store it in a dictionary
        list.append({
            "title": f.readline().rstrip("\n"),  # First line is the title
            "name": f.readline().rstrip("\n"),   # Second line is the name
            "date": f.readline().rstrip("\n"),   # Third line is the date
            "feedback": f.read().rstrip("\n")    # Remaining text is the feedback
        })

# Iterate through the feedback list and send each item as a POST request
for item in list:
    resp = requests.post('http://127.0.0.1:80/feedback/', json=item)  # Sending data as JSON
    
    # Check if the request was successful (HTTP status code 201 indicates success)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))  # Raise an error if POST request fails
    
    # Print the ID of the created feedback entry
    print('Created feedback ID: {}'.format(resp.json()["id"]))
```

## Expected Output

Upon running the script successfully, the feedback will be uploaded, and you'll see output similar to:

```
Created feedback ID: 1
Created feedback ID: 2
...
```

## Screenshots

### 1. Customer Feedback Files

### 2. Running the Script

### 3. Feedback Displayed on Website
![Automating_Customer_Feedback_1](https://github.com/user-attachments/assets/4ce4e88b-b251-4298-ae4a-865146037df1)
![Automating_Customer_Feedback_2](https://github.com/user-attachments/assets/c178b86f-edc3-453f-abea-5cc02dd275c5)
![Automating_Customer_Feedback_3](https://github.com/user-attachments/assets/03cdb8e3-2832-4c48-930b-af07e447f2c6)
![Automating_Customer_Feedback_4](https://github.com/user-attachments/assets/eaa3cb16-c52f-4504-807d-3a7fb304ea38)
![Automating_Customer_Feedback_5](https://github.com/user-attachments/assets/45bc7bb2-e67a-4cc1-a9a1-fd40f37ecdd5)
![Automating_Customer_Feedback_6](https://github.com/user-attachments/assets/06acd4f4-37be-499a-911a-a5480a795e2a)




## Troubleshooting

- If you receive a `ConnectionError`, check that the web service is running.
- If a `POST error status` appears, verify the API endpoint and the request format.
- Ensure that the `.txt` files are correctly formatted.

## License

This project is licensed under the MIT License.

💡 Contributions are welcome! If you have any improvements or suggestions, feel free to fork the repository and submit a pull request. 🚀

## Author

Shlok Sharma






