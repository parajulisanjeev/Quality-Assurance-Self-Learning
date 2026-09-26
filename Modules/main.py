import calculator_module

print("Simple Calculator")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Greatest Number")

choice = int(input("Choose calculation (1-5): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Addition =", calculator_module.add(num1, num2))

elif choice == 2:
    print("Subtraction =", calculator_module.subtract(num1, num2))

elif choice == 3:
    print("Multiplication =", calculator_module.multiply(num1, num2))

elif choice == 4:
    print("Division =", calculator_module.divide(num1, num2))

elif choice == 5:
    print("Greatest =", calculator_module.greatest(num1, num2))

else:
    print("Invalid choice")