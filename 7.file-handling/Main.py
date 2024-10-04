
# reading
"""
Reads the contents of the 'example.txt' file and prints the contents to the console.
"""
file = open('example.txt', 'r') # r for read
content = file.read()
print(content)
file.close()

# writing
"""
Writes the string 'Hello, world!' and the string 'This is new word' to the 'example.txt' file. If the file does not exist, it will be created.
"""
file = open('example.txt', 'w') # w for write
file.write('Hello, world!')
file.write("This is new word")
print(content)
file.close()

# add
"""
Appends the string 'Adding new content' to the 'example.txt' file. If the file does not exist, it will be created.
"""
file = open('example.txt', 'a') # a for append or add
file.write('Adding new content')
print(content)
file.close()

with open('example.txt', 'r') as contents:
    content2 = contents.read()
    print(content2)