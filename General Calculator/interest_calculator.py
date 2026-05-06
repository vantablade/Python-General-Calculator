def run_interest_calculator():
    print("***INTEREST CALCULATOR***")

    while True:
        interest_type = input("""
What type of interest do you want to calculate:
1. Simple interest 
2. Compound interest
> """)

        if interest_type in ("1", "2"):
            break

        print("Invalid input. Please enter 1 or 2.")

    if interest_type == "1":
        p = float(input("Enter the principal amount: "))
        r = float(input("Enter the interest rate (%): "))
        t = float(input("Enter the time period in years: "))
        simple_interest = (p * r * t) / 100
        print(f"Simple interest is: {simple_interest:.2f}")
        print(f"Final amount is {simple_interest + p:.2f}")

    elif interest_type == "2":
        p = float(input("Enter the principal amount: "))
        r = float(input("Enter the interest rate (%): "))
        n = float(input("Enter total times interest is compounded: "))
        compound_interest = p * (1 + (r / 100)) ** n
        print(f"Compound interest is {compound_interest:.2f}")
