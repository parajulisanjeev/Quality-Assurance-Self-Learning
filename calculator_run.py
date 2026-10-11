from calculator_class import Calculator

obj = Calculator()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
obj.add(a, b)
obj.subtract(a, b)
obj.multiply(a, b)
try:
    obj.divide(a, b)
except ValueError as e:
    print(e)  