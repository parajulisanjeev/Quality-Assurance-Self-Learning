def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def greatest(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both are equal"