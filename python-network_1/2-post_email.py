import requests
import sys
import subprocess
import time

# Start the Flask web server in the background
web_server_process = subprocess.Popen(["python3", "web_server.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(5)  # Wait for the server to start

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

# Stop the web server
web_server_process.terminate()
