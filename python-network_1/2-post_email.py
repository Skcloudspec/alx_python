```python
#!/usr/bin/env python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    response = requests.post(url, data=email)
    print("Email: {}".format(sys.argv[2]))
    print("[{}]".format(response.status_code))
    print(response.text.strip())
```
