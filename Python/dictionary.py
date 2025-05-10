#dictionary is a class that contains the dictionary of words
#and the methods to add, remove and search for words in the dictionary
#dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#written in {} brackets
#dictionary is unordered, so we cannot access the elements of a dictionary using index  
#
my_dict={"name":"pallavi","age":24}
print(my_dict)
print(type(my_dict)) # dictionary is mutable
#dictionary is mutable, so we can change the value of a dictionary after it is created
print(my_dict["name"]) # access the value of the key "name"
print(my_dict["age"]) # access the value of the key "age"
print(my_dict.get("name")) # access the value of the key "name"
print(my_dict.get("age")) # access the value of the key "age"
print(my_dict.keys()) # access the keys of the dictionary
print(my_dict.values()) # access the values of the dictionary
print(my_dict.items()) # access the items of the dictionary

new_dict=my_dict.copy() # copy the dictionary to new_dict
print(new_dict) # print the new dictionary

my_dict.pop("name") # remove the key "name" from the dictionary
print(my_dict) # print the dictionary after removing the key "name"

for key in my_dict: # iterate over the keys of the dictionary
    print(key,":",my_dict[key]) # print the key

my_dict.update({"name":"pallavi","class":23}) 
# update the dictionary with the key "name" and value "pallavi"
print(my_dict) # print the dictionary after updating the key "name" and value "pallavi"


# Example: Nested Dictionary
nested_dict = {
    "student1": {"name": "Alice", "age": 20, "grade": "A"},
    "student2": {"name": "Bob", "age": 22, "grade": "B"},
    "student3": {"name": "Charlie", "age": 21, "grade": "A"},
}

# Accessing nested dictionary elements
print(nested_dict["student1"]["name"])  # Output: Alice
print(nested_dict["student2"]["grade"])  # Output: B

# Adding a new student to the nested dictionary
nested_dict["student4"] = {"name": "Diana", "age": 23, "grade": "C"}
print(nested_dict)

# Iterating through the nested dictionary
for student, details in nested_dict.items():
    print(f"{student}:")
    for key, value in details.items():
        print(f"  {key}: {value}")