```python
#!/usr/bin/env python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    response = requests.post(url, data=email)
    output = '{0} with email={1}'.format(url, sys.argv[2])
    print("Correct output - case: request {}".format(output))
    print("[{}]".format(response.status_code))
    print(response.request.url.replace(' ', ''))
````
