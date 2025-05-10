def add(x,y):
    return x + y

x= 5
y= 10
result= add(x,y)
print("The sum of {} and {} is {}".format(x,y,result))
# The sum of 5 and 10 is 15

def login(username, password):
    if username == 'admin' and password == 'admin':
        return True
    else:
        return False

username = input("Enter username: ")
password = input("Enter password: ")

result = login(username, password)
print("Login successful:", result)  # Login successful: True
# True
# False