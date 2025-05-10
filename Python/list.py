# List is a collection which is ordered and changeable. Allows duplicate members.
# list is ordered
# list is mutable
# list is iterable
# list is indexed
# list is ordered collection of items
# list is mutable, so we can change the value of a list after it is created 
# list is iterable, so we can iterate over the elements of a list




my_list=[1,2,3,4,5,6,'pallavi','Rajnish','pallavi','Rajnish',True,False]
print(my_list)
print(type(my_list))

my_list.append('vinisha')
print(my_list)

my_list.insert(2,'vinisha') # inserts 'vinisha' at index 2
print(my_list)

my_list.remove('vinisha') # removes the first occurrence of 'vinisha'
print(my_list)

my_list.pop(2)
print(my_list)  #removes the element at index 2

my_list[4]=100 # replaces the element at index 4 with 100
print(my_list)

# Example of iterating through a list
for item in my_list:
    print(item)

# Example of slicing a list
sliced_list = my_list[2:6]
print("Sliced List:", sliced_list)

# Example of checking if an element exists in the list
if 'pallavi' in my_list:
    print("'pallavi' is in the list")

# Example of finding the length of the list
print("Length of the list:", len(my_list))

# Example of sorting a list (only works if all elements are of the same type)
numeric_list = [5, 2, 9, 1, 7]
numeric_list.sort()
print("Sorted List:", numeric_list)