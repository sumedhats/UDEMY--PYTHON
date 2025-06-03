# Q1. Print a Poem

# Write a program that prints this poem exactly as shown (use \n for new lines):

# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
print("Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.")
# The following code has errors. Fix them to run correctly:

# print "Hello students!"
# print("Today we'll learn about 'strings')
# print('Don't forget to bring your laptop")
# print("Good Luck!)
print ("Hello students!")
print("Today we'll learn about 'strings'")
print("Don't forget to bring your laptop")
print("Good Luck!")
# Ask for a user’s favorite color and animal, then print:

# Your superhero name could be Blue Tiger!
# Only replace "Blue" and "Tiger" with their inputs.
color = input("what is ur favourite color")
animal = input ("what is your  favourite animal")
print(f"your superhero name could me {color}{animal}!")
# Variable Swap Challenge

# Swap values between three variables without using the original values directly:

# a = "apple"
# b = "banana"
# c = "cherry"
#  Swap: a -> cherry, b -> apple, c -> banana
a = "cherry"
b = "apple"
c = "banana"
# Q5. Greet the User

# Ask for the user’s name and age. Print:

# Hello, Alex! You are 20 years old.
name = input (" what is your name")
age = input (" what is your age")
print(f"Hello, {name}! You are {age} years old.")
#  Length of City Name

# Take input of a city name and print how many letters it has.
city = input("enter the name of a city") 
num = len(city)
print(f"The city name has {num} letters.")
# Q7. Initials Generator

# Ask for the user's first name and last name and print their initials:

# Input:
# First Name: Harry
# Last Name: Potter
# Output:
# Your initials are: H.P.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
initials = f"{first_name[0].upper()}.{last_name[0].upper()}"
print(f"Your initials are: {initials}")
# Q8. Fix the Code

# The code below has logic and syntax issues. Fix it:

# name = input("Enter your name)
# print("Hi" + name + "! How are you?)
name = input("Enter your name: ")
print("Hi " + name + "! How are you?")
# Q9. Fix and Improve

# The following program is meant to calculate the length of the full name:

# first = input("What is your first name? ")
# last = input("What is your last name? ")
# full = first + last
# length = full
# print("Your full name is " + full)
# print("It is " + length + " letters long.")
first = input("What is your first name? ")
last = input("What is your last name? ")
full = first + " " + last  # Add a space between first and last name
length = len(full)  # Calculate the length of the full name
print("Your full name is " + full)
print("It is " + str(length) + " letters long.")  # Convert length to string for concatenation
# Q1. String Indexing

# Write a program that:

# Asks the user for a word.
# Prints the first and last letter using indexing.
# Example Input: banana
# Example Output:

# First letter: b  
# Last letter: a
name = input("what is the word")
first_letter = name[0]
last_letter = name[-1]
print(f"First letter: {first_letter}")
print(f"Last letter: {last_letter}")
# Q2. Reverse Indexing

# Use negative indexing to print the second-to-last letter of "Elephant".
word = "elephant"
second_to_last_letter = word[-2]
print(f"The second-to-last letter of '{word}' is: {second_to_last_letter}")
# Combine Strings and Numbers

# Fix and run this code:

# num1 = "100"
# num2 = "200"
# # Add these as numbers, not strings
num1 = "100"
num2 = "200"
sum_result = int(num1) + int(num2)  # Convert strings to integers before adding
print("The sum of " + num1 + " and " + num2 + " is: " + str(sum_result))  # Convert sum to string for concatenation
# Type Check

# Ask the user to enter any value. Print what type of data it is using type().
value = input("Enter any value: ")
print("The type of the entered value is:", type(value))
# Q5. Data Conversion

# Convert the following and print results:

# "123" → int
# 4.56 → str
# True → int
num_str = "123"
num_int = int(num_str)  # Convert string to integer
float_num = 4.56
str_num = str(float_num)  # Convert float to string
bool_value = True
int_bool = int(bool_value)  # Convert boolean to integer
print(f'"{num_str}" as int is: {num_int}')
print(f'{float_num} as str is: "{str_num}"')
print(f'{bool_value} as int is: {int_bool}')
# Q6. Quick Calculator

# Take two numbers as input from the user. Print their:

# Sum
# Difference
# Product
# Power
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2
power_result = num1 ** num2
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {product_result}")
print(f"Power: {power_result}")
# Q7. BMI Calculator with Input

# Write a program that:

# Takes height and weight from user input.
# Calculates and prints the BMI.
# Bonus: Print a message like "Your BMI is 25. You are healthy."
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}.", end=" ")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You are healthy.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
elif bmi >= 30:
    print("You are obese.")
# Q8. Length & Type

# Ask the user to input a password. Print:

# Its length
# Its data type
# First character
password = input("Enter your password: ")
password_length = len(password)
password_type = type(password)
first_character = password[0]
print(f"Password Length: {password_length}")
print(f"Password Type: {password_type}")
print(f"First Character: {first_character}")
# Q9. Expression Challenge

# Predict and print the result of this expression:

# print(5 + 3 * 2 - 4 / 2)
# Then explain why the result is what it is (order of operations).
result = 5 + 3 * 2 - 4 / 2
print("The result of the expression 5 + 3 * 2 - 4 / 2 is:", result)
# 10. Format Print

# Use f-strings to print the following:

# Student: Alice
# Age: 14
# Passed: True
# The values should be from variables.
student_name = "Alice"
age = 14
passed = True
print(f"Student: {student_name}\nAge: {age}\nPassed: {passed}")
# Case 1: Amusement Park Ride Check

# Write a program that:

# Asks the user for their age and height.
# Allows only users above 12 years and taller than 150 cm to ride the attraction.
# Others get a “Sorry” message.
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
if age > 12 and height > 150:
    print("You can ride the attraction!")
else:
    print("Sorry, you cannot ride the attraction.") 
#     Case 2: Grading System

# Write a program that takes the exam score as input and prints:

# 90–100: "Grade A"
# 80–89: "Grade B"
# 70–79: "Grade C"
# 60–69: "Grade D"
# Below 60: "Fail"
score = int(input("Enter your exam score: "))
if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
elif 60 <= score < 70:
    print("Grade D")
elif score < 60:
    print("Fail")
#     Case 3: Even/Odd + Multiple Check

# Take a number input:

# Print if it's even or odd.
# Also check if it is a multiple of 3 or 5 and say so.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
if number % 3 == 0:
    print(f"{number} is a multiple of 3.")
if number % 5 == 0:
    print(f"{number} is a multiple of 5.")
#     Case 4: BMI Calculator with Category (Expanded)

# Add more categories:

# Under 16: “Severely underweight”
# 16–18.5: “Underweight”
# 18.5–25: “Normal”
# 25–30: “Overweight”
# 30+: “Obese”
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
if bmi < 16:
    category = "Severely underweight"
elif 16 <= bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
elif bmi >= 30:
    category = "Obese"
print(f"Your BMI is {bmi:.2f}. You are classified as: {category}")
# Case 5: Cinema Ticket System

# Ask for age and time of the show (day or night):

# Age < 12: $5
# 12–18: $7
# Adult: $10
# If it’s a night show, add $2 to the ticket.
# Also ask:

# Popcorn? If yes, add $3
age = int(input("Enter your age: "))
show_time = input("Is the show at night? (yes/no): ").strip().lower()
popcorn = input("Do you want popcorn? (yes/no): ").strip().lower()
if age < 12:
    ticket_price = 5
elif 12 <= age <= 18:
    ticket_price = 7
elif age > 18:
    ticket_price = 10
if show_time == "yes":
    ticket_price += 2
if popcorn == "yes":
    ticket_price += 3
print(f"Your total ticket price is: ${ticket_price}")
# Case 6: Coffee Machine Order

# Ask:

# Size: small (s), medium (m), large (l)
# Add milk? y/n → $1
# Add sugar? y/n → $0.5
# Calculate and print the bill based on:

# Small = $2
# Medium = $3
# Large = $4
size = input("Enter coffee size (s/m/l): ").strip().lower()
milk = input("Add milk? (y/n): ").strip().lower()
sugar = input("Add sugar? (y/n): ").strip().lower()
if size == 's':
    price = 2
elif size == 'm':
    price = 3
elif size == 'l':
    price = 4
if milk == 'y':
    price += 1
if sugar == 'y':
    price += 0.5
print(f"Your total coffee bill is: ${price:.2f}")
# Case 7: Speed Checker

# Take speed input from user.

# If < 60 → “Safe”
# If between 60 and 80 → “Caution”
# If over 80 → “Over-speeding! Ticketed.”
speed = int(input("Enter your speed: "))
if speed < 60:
    print("Safe")
elif 60 <= speed <= 80:
    print("Caution")
elif speed > 80:
    print("Over-speeding! Ticketed.")
#     Case 8: Eligibility Checker

# Ask for:

# Age
# Nationality
# Years of experience
# Determine if the person is eligible for:

# A driving license
# A job (based on age and experience)
# Voting (age ≥ 18)
print("Welcome to the Eligibility Checker!")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").lower()
experience = int(input("Enter your years of work experience: "))
print("\nChecking eligibility...\n")
if age >= 18:
    print(" You are eligible for a driving license.")
else:
    print(" You are NOT eligible for a driving license (Minimum age is 18).")
if age >= 21 and experience >= 2:
    print(" You are eligible to apply for the job.")
elif age >= 21:
    print("You are not eligible for the job (Need at least 2 years of experience).")
else:
    print(" You are NOT eligible for the job (Minimum age is 21).")
if age >= 18 and nationality == "indian":
    print(" You are eligible to vote.")
elif age >= 18:
    print(" You are not eligible to vote in Nepal (only Nepali citizens can vote).")
else:
    print("You are NOT eligible to vote (Minimum age is 18).")
#     Case 9: Simple Login System

# Ask for username and password.

# If username == “admin” and password == “1234”, print “Login successful”
# Else, print “Access denied”
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Access denied")
#     Case 10: Pizza Order with Offer

# Same as your pizza program but add:

# If user orders large and wants cheese, give $2 off
# If user orders medium with no cheese, give free drink
size = input("Enter pizza size (small/medium/large): ").strip().lower()
cheese = input("Do you want cheese? (yes/no): ").strip().lower()
drink = input("Do you want a drink? (yes/no): ").strip().lower()
if size == "small":
    price = 8
elif size == "medium":
    price = 10
    if cheese == "no":
        print("You get a free drink with your medium pizza!")
        drink_price = 0
    else:
        drink_price = 1.5
elif size == "large":
    price = 12
    if cheese == "yes":
        price -= 2
    drink_price = 1.5
if drink == "yes":
    price += drink_price
print(f"Your total pizza order price is: ${price:.2f}")



    
 
