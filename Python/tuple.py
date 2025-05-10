my_tuple=(1,2,3,4,5,6,7,8,9,10,'pallavi','Rajnish','pallavi','Rajnish',True,False)
print(my_tuple)
print(type(my_tuple)) # tuple is immutable
#tupple is immutable, so we cannot change the value of a tuple after it is created
#tupple is immutable, so we cannot change the value of a tuple after it is created
#difference between list and tuple is that list is mutable and tuple is immutable
#the use of tuple is to store the data which is not going to be changed in future
#tuplle use in real time is to store the data which is not going to be changed in future

print("elements of tuple are:",my_tuple[2])
print(len(my_tuple)) # length of tuple

print("elements of tuple are:",my_tuple[-1]) # slicing of tuple


# Example of tuple unpacking
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = my_tuple
print("Unpacked values:", a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p)

# Example of nested tuple
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Nested tuple:", nested_tuple)

# Accessing elements in a nested tuple
print("Element from nested tuple:", nested_tuple[1][2])

# Checking if an element exists in a tuple
print("Is 'pallavi' in my_tuple?", 'pallavi' in my_tuple)

# Counting occurrences of an element in a tuple
print("Count of 'pallavi' in my_tuple:", my_tuple.count('pallavi'))

# Finding the index of an element in a tuple
print("Index of 'Rajnish' in my_tuple:", my_tuple.index('Rajnish'))