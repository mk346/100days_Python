print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
friends = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_payable = (tip / 100) * bill
#total_tip_payable = tip_payable_each *   friends
total_bill = tip_payable + bill
bill_payable_each = round(total_bill / friends, 2)

print("Each person should pay: $"+str(bill_payable_each))