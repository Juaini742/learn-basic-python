
# how to create array in python
students = ["Joko", "Dody", "Alice", "John"]
for student in students:
    print(student)

# with index
for index, value in enumerate(students):
    print(f"{index} = {value}")


for i in range(10): 
    print(i)

print("--LIMIT--")

count = 5
while count < 8:
    print(count)
    count += 1

print("--LIMIT--")

for j in range(5):
    if j == 3:
        break
    print(j)

print("--LIMIT--")

for i in range(8):
    if i == 3:
        continue  
    print(i)
