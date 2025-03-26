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