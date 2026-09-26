print("Simple Calculator")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Compare Greatest Number")

choice = int(input("Choose calculation (1-5): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    result = num1 + num2
    print("Addition =", result)

elif choice == 2:
    result = num1 - num2
    print("Subtraction =", result)

elif choice == 3:
    result = num1 * num2
    print("Multiplication =", result)

elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print("Division =", result)
    else:
        print("Cannot divide by zero")

elif choice == 5:
    if num1 > num2:
        print(num1, "is greatest")
    elif num2 > num1:
        print(num2, "is greatest")
    else:
        print("Both numbers are equal")

else:
    print("Invalid choice")