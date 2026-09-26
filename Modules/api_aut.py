# API Automation using requests module

import requests

# print(dir(requests))
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print(response.status_code)
print(response.json())