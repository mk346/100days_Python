#liftime left calculator
age = int(input("What is your current age? "))
target_years = 90
remaining_years = target_years - age
days_left = remaining_years * 365
months_left = remaining_years * 12
weeks_left = remaining_years * 52

print("You have " +str(days_left) +" days, "+str(weeks_left)+" weeks, and "+str(months_left)+" months left.")
