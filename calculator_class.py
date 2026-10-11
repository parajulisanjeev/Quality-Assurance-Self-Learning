class Calculator:
    def add(self, a, b):
        print("Addition:", a + b)

    def subtract(self, a, b):
        print("Subtraction:", a - b)

    def multiply(self, a, b):
        print("Multiplication:", a * b)

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        print("Division:", a / b)

