# BMI Calculator
# bmi = weight/height * height (m * m) <-??


height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

ht = float(height)
wt = float(weight)

print( type(ht))

bmi = (wt) / ht **2

print(round(bmi))

print(int(bmi))
