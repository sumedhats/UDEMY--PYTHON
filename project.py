# PROJECT 1
print("Welcome to the Band Name Generator")
a = input("what is the name of the city you grew up in? \n")
b = input("what is the name of your pet? \n")
print("Your band name could be " + a + " " + b)
# PROJECT 2
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? "))
people_count = int(input("How many people to split the bill? "))
tip_amount = total_bill * (tip_percentage / 100)
total_amount = total_bill + tip_amount
amount_per_person = total_amount / people_count
amount_per_person = round(amount_per_person, 2)
print(f"Each person should pay: ${amount_per_person}")
 

