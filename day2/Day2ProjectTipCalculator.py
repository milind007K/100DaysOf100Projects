# Tip Calculator Project
print("Welcome to tip calculator")
bill = float(input("What was the total bill ? $"))
tip = int(input("what percentage tip would you like to give ? 10 , 12 , 15 "))
people = int(input("how many people do you split the bill ? "))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)

bill_with_split = bill_with_tip / people
print(bill_with_split)
