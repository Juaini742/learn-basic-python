# Dalam membuat function pada python diawali dengan def

# def nama_function():
#     print("TODO")
# nama_function()

def sayHello(name) :
    return f"Hello, {name}"

print(sayHello("Dody"))

def countPlus(a, b):
    return a + b

print(countPlus(2, 10))

def greet(name="John"):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet())

def total(*number):
    return sum(number)
print(total(1, 2, 3, 5, 10))

def names(*students):
    return students
print(names("Dody", "Rahmad", "Rahmawan"))

def info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
info(name="Alice", age=25, city="Wonderland")

def factorial(n):
    if n == 1 :
        return 1
    else : 
        return n * factorial(n - 1)
print(factorial(3))

plusSum = lambda a, b: a + b
print(plusSum(5, 10))  # Output: 15

# function with array
def info(*people):
    for name, age in people:
        print(f"Name: {name}, Age: {age}")

info(('John', 21), ('Alice', 22), ('Bob', 25))

def studentsArray(students):
    for student in students:
      print(f"My name is {student['name']}, and my age is {student['age']}")

students = [
    {"name": "John","age": 21},
    {"name": "Alice","age": 22},
    {"name": "John","age": 30},
]
studentsArray(students)

# anonymous function
check = lambda x: "Greet then 10" if x > 10 else "Less then or equal to 10"

print(check(90))
print(check(8))

x = 11
result = "Greater than 20" if x > 20 else "Greater than 10" if x > 10 else "10 or less"
print(result) 


