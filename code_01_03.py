import requests

url = 'https://api.github.com/user'
response = requests.get(url)
print(response.json())

response_auth = requests.get(url, headers={'Authorization': 'Bearer 44bc4d7853e7632e12bdbcdd3ffa6389c63a148e'})

git_response = response_auth.json()

for keys in git_response.keys():
	print(keys)

print(git_response['id'])
