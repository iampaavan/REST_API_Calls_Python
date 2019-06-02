import requests

url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)

json_data = response.json()

my_list = []

for photo in json_data:
	my_list.append(photo['url'])
	
print(my_list)

print(f"Length of the list: {len(my_list)}")

my_set = set(my_list)
print(f"Length of the set: {len(my_set)}")

dict = dict()

for photo in json_data:
	dict[photo['url']] = dict.get(photo['url'], 0) + 1

print(dict)

for keys, values in dict.items():
	if values > 1:
		print(keys)
