import requests 

response = requests.get('https://jsonplaceholder.typicode.com/users')
print("status code: ",response.status_code)
data=response.json()
print("data: ",data)
print("data type: ",type(data))
print("street: ",data['address']['street'])
print("city: ",data['address']['city'])
print("zipcode: ",data['address']['zipcode'])
print("geo: ",data['address']['geo'])
print("geo lat: ",data['address']['geo']['lat'])
print("geo lng: ",data['address']['geo']['lng'])

