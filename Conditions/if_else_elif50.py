#50. Write a program to create menu-driven arithmetic operations using if-elif-else.


# Menu-driven arithmetic operations program
print("--- Arithmetic Menu ---\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = input("Enter choice (1-4): ")

# Validating input and performing calculations
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Selection Logic using if-elif-else
    if choice == '1': print(f"Result: {num1 + num2}")
    elif choice == '2': print(f"Result: {num1 - num2}")
    elif choice == '3': print(f"Result: {num1 * num2}")
    elif choice == '4':
        # Division by zero check
        print(f"Result: {num1 / num2}" if num2 != 0 else "Error: Division by zero")
else:
    print("Invalid choice")
