# process-txt-upload-web-service
A script to convert the reviews stored as .txt files and process them into Python dictionaries, then upload the data onto the company’s website (in this project, using Django)
Automating Customer Feedback Processing with Python

📌 Project Overview

This project automates the process of reading customer feedback stored in text files and uploading them to a Django-powered web service. The script reads customer reviews, structures them into Python dictionaries, and submits them via a REST API.

📂 Project Structure

├── run.py  # Main Python script for processing and uploading feedback
├── /data/feedback/  # Directory containing customer feedback text files

🚀 Features

Automatic file scanning: Reads all .txt feedback files from a specified directory.

Data extraction & structuring: Converts unstructured text files into JSON-formatted dictionaries.

Web service integration: Sends feedback data to a Django REST API for storage.

Status handling: Checks server responses to ensure successful uploads.

🔧 Prerequisites

Before running the script, ensure you have:

Python 3 installed

Django web service running

requests library installed (pip install requests)

💻 Usage

Clone the Repository:

git clone https://github.com/yourusername/customer-feedback-automation.git
cd customer-feedback-automation

Navigate to the Home Directory & Grant Execution Permission:

chmod +x run.py

Run the Script:

./run.py

Verify Uploaded Feedback:

Open the web browser and navigate to http://<corpweb-external-IP>/feedback/ to check the posted reviews.

📜 Code Explanation

import os  # For file handling
import requests  # For making HTTP requests

BASEPATH = '/data/feedback/'  # Directory containing feedback files
folder = os.listdir(BASEPATH)  # List all files in the directory

feedback_list = []

for file in folder:
    with open(BASEPATH + file, 'r') as f:
        feedback_list.append({
            "title": f.readline().strip(),
            "name": f.readline().strip(),
            "date": f.readline().strip(),
            "feedback": f.read().strip()
        })

for feedback in feedback_list:
    response = requests.post('http://<corpweb-external-IP>/feedback/', json=feedback)
    if response.status_code == 201:
        print(f"✅ Feedback uploaded: {feedback['title']}")
    else:
        print(f"❌ Failed to upload feedback: {response.status_code}")

📸 Screenshots

Feedback files stored in /data/feedback/ 📂

Script execution showing successful uploads 🖥️

Website displaying posted customer feedback 🌐

![Automating_Customer_Feedback_1](https://github.com/user-attachments/assets/4ce4e88b-b251-4298-ae4a-865146037df1)
![Automating_Customer_Feedback_2](https://github.com/user-attachments/assets/c178b86f-edc3-453f-abea-5cc02dd275c5)
![Automating_Customer_Feedback_3](https://github.com/user-attachments/assets/03cdb8e3-2832-4c48-930b-af07e447f2c6)
![Automating_Customer_Feedback_4](https://github.com/user-attachments/assets/eaa3cb16-c52f-4504-807d-3a7fb304ea38)
![Automating_Customer_Feedback_5](https://github.com/user-attachments/assets/45bc7bb2-e67a-4cc1-a9a1-fd40f37ecdd5)
![Automating_Customer_Feedback_6](https://github.com/user-attachments/assets/06acd4f4-37be-499a-911a-a5480a795e2a)



🛠️ Troubleshooting

If the script fails to upload, check the API endpoint and ensure the web service is running.

Use print(response.text) to debug unexpected server responses.

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

💡 Contributions are welcome! If you have any improvements or suggestions, feel free to fork the repository and submit a pull request. 🚀

