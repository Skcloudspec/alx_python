from urllib.parse import urlencode
import requests
import sys

# Construct the URL with parameters using urllib.parse.urlencode
base_url = "http://0.0.0.0:5050"
params = {"email": "test@test.com"}

url = f"{base_url}?{urlencode(params)}"
print(url)

# Send the POST request
response = requests.post(url)

# Retrieve the URL and email address from the command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Construct the payload
payload = {'email': email}

# Send the POST request
response = requests.post(url, data=payload)

# Print the email address and the body of the response
print("Your email is:", email)
print(response.text)
