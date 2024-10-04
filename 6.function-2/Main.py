from functools import reduce

def add(x, y):
    return x + y
add_lambda = lambda x, y: x + y

print(add(10, 2))
print(add_lambda(10, 2))

print("+++++++++++++++++")

def square(x):
    return x ** 2

numbers = [1,2,3,4,5]

# map
"""
Maps the `square` function over the `numbers` list to create a new list of squared numbers.

Args:
    numbers (list[int]): The list of numbers to square.

Returns:
    list[int]: A new list containing the squared values of the `numbers` list.
"""

"""
Maps the lambda function `lambda x: x ** 2` over the `numbers` list to create a new list of squared numbers.

Args:
    numbers (list[int]): The list of numbers to square.

Returns:
    list[int]: A new list containing the squared values of the `numbers` list.
"""
squared_numbers = map(square, numbers)
print(list(squared_numbers))

# map with lambda
square_numbers_lambda = map(lambda x: x ** 2, numbers)
print(list(square_numbers_lambda))

print("+++++++++++++++++")

# filter
"""
Filters the `numbers` list to only include even numbers using the `is_even` function.

Args:
    numbers (list[int]): The list of numbers to filter.

Returns:
    list[int]: A new list containing only the even numbers from the `numbers` list.
"""

"""
Filters the `numbers` list to only include even numbers using a lambda function.

Args:
    numbers (list[int]): The list of numbers to filter.

Returns:
    list[int]: A new list containing only the even numbers from the `numbers` list.
"""
def is_even(x):
    return x % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

even_numbers_lambda = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers_lambda))

print("+++++++++++++++++")

# reduce
"""
Applies the `add` function to reduce the `numbers` list to a single total value.

Args:
    x (int): The first number to add.
    y (int): The second number to add.

Returns:
    int: The sum of `x` and `y`.
"""
def add(x, y):
    return x + y

"""
Reduces the `numbers` list to a single total value using the `add` function.

Args:
    numbers (list[int]): The list of numbers to sum.

Returns:
    int: The total sum of the `numbers` list.
"""
total = reduce(add, numbers)

"""
Reduces the `numbers` list to a single total value using a lambda function.

Args:
    numbers (list[int]): The list of numbers to sum.

Returns:
    int: The total sum of the `numbers` list.
"""
total_lambda = reduce(lambda x, y: x + y, numbers)
def add (x, y):
    return x + y

total = reduce(add, numbers)
print(total)

total_lambda = reduce(lambda x, y: x + y, numbers)
print(total_lambda)

