weight = float(input("Enter Weight: "))
height = 1.8

BMI = weight / height**2

print("Your BMI is: ", round(BMI,2))

if BMI <= 16.5:
    print("You are Severly Underweight")

elif BMI == 16.6 or BMI <= 18.3:
    print("You are Underweight")

elif BMI == 18.4 or BMI <= 25:
    print("You are Normal")

elif BMI == 26 or BMI <= 30:
    print("You are Overweight")

elif BMI == 31 or BMI <= 35:
    print("You are Obese Class 1")

elif BMI == 36 or BMI <= 40:
    print("You are Obese Class 2")

elif BMI == 41 or BMI <= 45:
    print("You are Severly Obese")

elif BMI == 46 or BMI <= 50:
    print("You are Morbidity Obese")

elif BMI == 51 or BMI <= 61:
    print("You are Super Obese")

else:
    print("You are Hyper Obese")