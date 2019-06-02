import requests

url = 'https://api.github.com/user'
response = requests.get(url)
print(response.json())

response_auth = requests.get(url, headers={'Authorization': 'Bearer alphanumeric'})

git_response = response_auth.json()

for keys in git_response.keys():
	print(keys)

print(git_response['id'])
