import requests

url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
print(response.json())

json_payload = {
	'albumId': 1,
	'title': 'test',
	'url': 'example.com',
	'thumbnailUrl': 'example.com'
}

post_response = requests.post(url, json=json_payload)
print(post_response.json())

url_put = 'https://jsonplaceholder.typicode.com/photos/100'
put_response = requests.put(url_put, json=json_payload)
print(put_response.json())

delete_response = requests.delete(url_put)
print(delete_response.json())


