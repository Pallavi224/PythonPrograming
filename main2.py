import requests

# POST request
data = {"name": "John Doe", "age": 30, "city": "New York"}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print("POST response: ", response.json())

# GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts')
print("status code: ", response.status_code)
data = response.json()
print("data type: ", type(data))  # Should print <class 'list'>

# Access the first post
first_post = data[0]  # Access the first post in the list
print("First post title: ", first_post['title'])
print("First post body: ", first_post['body'])



