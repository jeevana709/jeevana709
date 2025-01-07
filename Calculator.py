def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def show_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    while True:
        show_menu()
        
        try:
            choice = int(input("Enter choice (1/2/3/4/5): "))
            
            if choice in [1, 2, 3, 4]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == 1:
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == 2:
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == 3:
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == 4:
                    print(f"{num1} / {num2} = {divide(num1, num2)}")

            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid input! Please select a valid option.")
        except ValueError:
            print("Invalid input! Please enter numerical values.")
        
if __name__ == "__main__":
    main()