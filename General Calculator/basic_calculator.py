def run_basic_calculator():
    print("***BASIC CALCULATOR***")
    n1 = float(input("Enter your first number: "))
    n2 = float(input("Enter the second number: "))
    operator = input("""
        Enter the operator you want to use: 
        Addition (+)
        Subtraction (-)
        Multiplication (*)
        Division (/)
        > """)

    if operator == "+":
        print(f"Result: {n1 + n2:.2f}")
    elif operator == "-":
        print(f"Result: {n1 - n2:.2f}")
    elif operator == "*":
        print(f"Result: {n1 * n2:.2f}")
    elif operator == "/":
        print(f"Result: {n1 / n2:.2f}")
    else:
        print("Invalid operator")
