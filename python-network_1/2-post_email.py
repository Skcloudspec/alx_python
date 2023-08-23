import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

# Ensure proper formatting of the URL and email
if not url.startswith("http://") and not url.startswith("https://"):
    url = "http://" + url
if not url.endswith("/"):
    url += "/"
if not email.startswith("email="):
    email = "email=" + email

url += "?" + email

response = requests.post(url)

print("Your email is:", email.split("=")[1])
print(response.text)
