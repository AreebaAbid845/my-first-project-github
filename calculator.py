def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def main():
    print("=== Welcome to the Calculator App ===")
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")

    choice = input("Choose operation (1/2): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    else:
        print("Invalid choice")

# This is my modification for the 2nd commit

if __name__ == "__main__":
    main()
