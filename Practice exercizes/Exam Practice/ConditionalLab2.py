weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in meters: "))

age = 16

bodyMassIndex = weight / (height**2)

if age >= 16:
    if bodyMassIndex < 18.5:
        print("Underweight")
    elif bodyMassIndex > 18.5 and bodyMassIndex < 24.9:
        print("Normal BMI")
    elif bodyMassIndex >= 25.0 and bodyMassIndex <= 29.9:
        print("Overweight")
    else:
        print("OBESE")
        