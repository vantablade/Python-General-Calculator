from basic_calculator import run_basic_calculator
from bmi_calculator import run_bmi_calculator
from currency_calculator import run_currency_calculator
from interest_calculator import run_interest_calculator

active = True

print("***GENERAL CALCULATOR***")

while active:
    yes_no = input("Do you want to perform a calculation (Y/N): ").lower()
    if yes_no == "y":  
        calculation_type = input("""
Enter the digit for the type of calculation you want:
1. Basic Calculator
2. Interest Calculator
3. BMI calculator
4. Currency calculator
5. EXIT
> """)
    elif yes_no == "n":
        print("Goodbye!")
        active = False
        continue
    else:
        print("Invalid input. Please enter Y or N.")
        continue

    if calculation_type == "1":
        run_basic_calculator()
    
    elif calculation_type == "2":
        run_interest_calculator()
    
    elif calculation_type == "3":
        run_bmi_calculator()
    
    elif calculation_type == "4":
        run_currency_calculator()
    elif calculation_type == "5":
        print("Goodbye!")
        active = False  

    else:
        print("Invalid choice, try again.")
