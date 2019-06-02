import requests

url = 'https://api.github.com/user'
response = requests.get(url)
print(response.json())

response_auth = requests.get(url, auth=('iampaavan', 'viratKohli153@'))
print(response_auth.json())

response_token = requests.get(url, headers={'Authorization': 'Bearer 44bc4d7853e7632e12bdbcdd3ffa6389c63a148e'})
print(response_token.json())

