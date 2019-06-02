import requests

url = 'https://api.github.com/user'
response = requests.get(url)
print(response.json())

response_auth = requests.get(url, auth=('yourusername', 'yourpassword'))
print(response_auth.json())

response_token = requests.get(url, headers={'Authorization': 'Bearer alphanumeric'})
print(response_token.json())

