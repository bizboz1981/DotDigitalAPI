import requests
import csv

url = "https://r1-api.dotdigital.com/v2/contacts/resubscribe-with-no-challenge"

# Load your CSV file
csv_file_path = "resubscribe_29012024.CSV"

# Function to read authorization code from file
def read_auth_token():
    with open("auth_token.txt", "r") as file:
        print(file.read().strip())

# Set your authorization token
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": read_auth_token()
}

# Function to make API request for each record
def update_email_permissions(email, first_name, last_name):
    payload = {
        "unsubscribedContact": {
            "email": email,
            "dataFields": [
                {
                    "key": "FIRST_NAME",
                    "value": first_name
                },
                {
                    "key": "LAST_NAME",
                    "value": last_name
                }
            ]
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)

# Open and read the CSV file
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Assuming your CSV has columns 'email', 'first_name', and 'last_name'
        email = row['email']
        first_name = row['first_name']
        last_name = row['last_name']

        # Make API request for each record
        update_email_permissions(email, first_name, last_name)
