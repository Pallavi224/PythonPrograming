import requests 


response = requests.get('https://jsonplaceholder.typicode.com/users')
print("status code: ", response.status_code)
data = response.json()
print("data: ", data)
print("data type: ", type(data))

# Access the first user's address
first_user = data[0]  # Access the first user in the list
print("street: ", first_user['address']['street'])
print("city: ", first_user['address']['city'])
print("zipcode: ", first_user['address']['zipcode'])
print("geo: ", first_user['address']['geo'])
print("geo lat: ", first_user['address']['geo']['lat'])
print("geo lng: ", first_user['address']['geo']['lng'])