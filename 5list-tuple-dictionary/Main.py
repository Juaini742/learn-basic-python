# here we will learn about array in python

# list
array_list = [1,2,3, "python", False, True]
print(array_list)
# print with index
print(array_list[0])
print(array_list[1])
print(array_list[2])
print(array_list[3])
print(array_list[4])
print(array_list[5])

# change value
array_list[0] = 10
print(array_list[0])

# adding new value in last of array
array_list.append("New value")
print(array_list[6])

print("++++++++++++++++")

# tuple
# Tuple is immutable array
array_tuple = (1,2,3, "Python", False, True)
print(array_tuple)


# print with index
print(array_tuple[0:3])

# change tuple value
# array_tuple[0] = 10  # this will give error

# loop tuple 
for item in array_tuple:
    print(item)

print("++++++++++++++++")

# dictionary
# dictionary is mutable array of key value pair
array_dict = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "is_married": False
}

print(array_dict)

# print with key
print(array_dict["is_married"])

# adding new key and value into dictionary
array_dict["country"] = "USA"
print(array_dict["country"])

# loop dictionary
for key, value in array_dict.items():
    print(f"{key}: {value}")

# dictionary array of object
students_dictionary = [
    {
        "name": "John",
        "age": 12,
        "hobby": "Reading"
    },
    {
        "name": "Alice",
        "age": 13,
        "hobby": "Swimming"
    },
    {
        "name": "Nathan",
        "age": 10,
        "hobby": "Reading"
    },
]

for student in students_dictionary:
    print(f"My name is {student['name']}, I am {student['age']} years old, and my hobby is {student['hobby']}")


# array of custom object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("John", 12),
    Student("Alice", 13),
]

for student in students:
    print(f"My name is {student.name}, I am {student.age} years old")