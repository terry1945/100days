# BMI Calculator
# bmi = weight/height * height (m * m) <-??
# m = inches * .0354
# k = lbs * 0.453

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

ht = float(height)
wt = float(weight)

#print( type(ht))

bmi = (wt) / ht **2

print(round(bmi))

print(int(bmi))

print("\n\nNow input in American and convert to metric")
ht_in = input("Enter your height in in: ")
wt_lb = input("Enter your weight in lbs: ")
ht = float(ht_in) * 0.354
wt = float(wt_lb) * 0.453

#convert to meters and kilos


bmi = (wt) / ht **2

print(bmi)
print(round(bmi))


