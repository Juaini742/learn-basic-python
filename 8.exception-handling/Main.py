

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Server internal error")
finally:
    print("finally condition")


def validate_age(age):
    if age < 0:
        raise ValueError("age is cannot to be negative")
    return True

try:
    validate_age(4)
except ValueError as e:
    print(f"error: {e}")