import requests
import pandas as pd
import datetime
import json

url = "https://r1-api.dotdigital.com/v2/contacts/unsubscribed-since/"
# Generate the current date and time
one_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)

# Format the date-time as per the desired format
formatted_datetime = one_month_ago.strftime("%Y-%m-%dT%H:%M:%S-00:00")

# Use the formatted date-time in the URL
url = f"https://r1-api.dotdigital.com/v2/contacts/unsubscribed-since/{formatted_datetime}"

with open('auth_token_2.txt', 'r') as file:
    auth_token_2 = file.read().strip()

# print(f"this should be the auth token: ", auth_token_2)
    

headers = {
    "accept": "application/json",
    "authorization": auth_token_2
}

response = requests.get(url, headers=headers) # Make a GET request to the URL
df = pd.DataFrame(response.json()) # Convert the JSON response to a DataFrame
print(f"Original df columns: ", df.columns)

# print(f"this is the original df: ", df.columns)

suppressedContact_df = df['suppressedContact'].apply(pd.Series)
print(f"This is suppressed_df: ", suppressedContact_df.columns)

new_df = pd.concat([suppressedContact_df, df['dateRemoved'], df['reason']], axis=1)

print(f"This is the new dataframe: ", new_df.columns)
new_df.to_csv('unsubscribed_contacts.csv', index=False) # Save the DataFrame to a CSV file  