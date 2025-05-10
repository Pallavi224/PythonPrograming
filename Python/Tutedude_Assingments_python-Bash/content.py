
'''Used dictionary and basic operations. Using if else:
3.Write to a File
Write a program to create a text file and write some content to it.

'''

# Program to create a text file and write some content to it

# Define the content to write
content = {
    "Name": "John Doe",
    "Age": 25,
    "Occupation": "Software Developer",
    "Hobbies": ["Reading", "Coding", "Traveling"]
}

# Convert dictionary to a formatted string
content_to_write = "\n".join([f"{key}: {value}" for key, value in content.items()])

# File name
file_name = "output.txt"

# Write content to the file
try:
    with open(file_name, "w") as file:
        file.write(content_to_write)
    print(f"Content successfully written to {file_name}")
except Exception as e:
    print(f"An error occurred: {e}")