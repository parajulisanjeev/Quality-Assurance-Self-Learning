import requests
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "userId": 1,
    "id": 1,
    "title": "My First Post",
    "body": "This is the content of my first post."
  }

# authorization={
#     "Authorization": "token 1234567890"
# }

# response = requests.post(url, json=payload, auth=authorization)

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())