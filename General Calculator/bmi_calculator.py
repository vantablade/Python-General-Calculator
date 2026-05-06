def run_bmi_calculator():
    print("***IBM CALCULATOR***")
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    age = int(input("Enter your age: "))
    gender = input("Gender: (M/F): ")
    bmi = weight / (height ** 2)

    if age > 19:
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Healthy"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

    if age <= 20:
        if bmi < 14:
            category = "Underweight"
        elif bmi < 22:
            category = "Healthy"
        elif bmi < 26:
            category = "Overweight"
        else:
            category = "Obese"

    print(f"Your BMI is {bmi:.2f}.")
    print(f"For your age, you are approximately {category}.")
