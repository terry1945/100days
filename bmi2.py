height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height*height)

if bmi < 18.5:
    print(f"Your BMI is : {round(bmi)}.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi)}, you are normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {round(bmi)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi)}, you are clinaclly obese")
       
