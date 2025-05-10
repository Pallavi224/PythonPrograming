
'''
Using file functions like write and open.
4. Read from a File
We used open in read mode and file.read to read and print to display.
'''
# Open the file in read mode
with open('output.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()
    # Print the contents to display
    print(content)
