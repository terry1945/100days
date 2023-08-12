# Life in Weeks to age 90

age = input("What is your cureent age? ")

timeleft = 90 - int(age)
days = timeleft * 365
weeks = timeleft * 52
months = timeleft * 12

#desired output

print(f"You have {days} days, {weeks} weeks, and {months} months until you are 90.")
