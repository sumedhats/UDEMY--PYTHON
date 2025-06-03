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
# PROJECT 3
 print('''888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888  ''')

print("Welcome to the treasure land. Your mission is to find the treasure.")
direction = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if direction == "left":
    action = input("You chose left. Do you want to swim or wait? Type 'swim' or 'wait': ").lower()
    if action == "wait":
        door = input("Great! Now choose a door: red, blue, or yellow: ").lower()
        if door == "red":
            print("You got caught by a witch.")
        elif door == "blue":
            print("You won!")
        elif door == "yellow":
            print("You got caught by a wizard.")
        else:
            print("Invalid choice.")
    elif action == "swim":
        print("Better luck next time.")
    else:
        print("Invalid choice.")
elif direction == "right":
    print("Better luck next time.")
else:
    print("Invalid choice.")
 # PROJECT 4
import random 
print("GAME")
print("WELCOME TO ROCK PAPER SISSOR GAME")
choose = input("Enter your choice rock, paper, scissor\n your choice : ")
choices = ["rock", "paper", "scissor"]
computer_choices = random.choice(choices)
print("Computer chose:", computer_choices)
if choose == computer_choices:
    print("It's a tie!")
elif (choose == "rock" and computer_choices == "scissor") or \
     (choose == "paper" and computer_choices == "rock") or \
     (choose == "scissor" and computer_choices == "paper"):
    print("You win!")
else:
    print("You lose!")
     



