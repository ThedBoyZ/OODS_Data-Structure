print(" *** BMI ***")
weight,height = input("Enter your weight(kg) and height(m) : ").split()
weight = float(weight)
height = float(height)
bmi = weight / (height*height)
if bmi < 18.5:
    print("Your status is : Below normal weight.")
elif bmi >= 18.5 and bmi < 25:
    print("Your status is : Normal weight.")
elif bmi >= 25 and bmi < 30:
    print("Your status is : Overweight.")
elif bmi >= 30 and bmi < 35:
    print("Your status is : Case I Obesity.")
elif bmi >= 35 and bmi < 40:
    print("Your status is : Case II Obesity.")
elif bmi >= 40:
    print("Your status is : Case III Obesity.")