# case 1
print("welcome to roller coaster")
height = int(input("enter ur height"))
if height > 180:
 print("get ready to the entusiasium")
else:
 print("better luch next time")
 #case 2
 num = int(input("enter a number"))
 if num % 2 ==0:
  print ("its even")
 else:
  print("its odd")
  # case 3
print("welcome to roller coaster")
height = int(input("enter ur height"))
age = int(input("enter ur age"))
if height > 180:
 print("Get ready to the entusiasium")
 if age >=18:
   print("ur ticket is 12$")
 else:
    print("ur ticket is 7$")
 # case 4
print("welcome to roller coaster")
height = int(input("enter ur height"))
age = int(input("enter ur age"))
if height > 180:
 print("Get ready to the entusiasium")
 if age < 12:
   print("ur ticket is 5$")
 elif age == 12 and age <18:
    print ("ur tichet is 7$")
 else:
    print("ur ticket is 12$")
else:
 print("better luch next time")
 # task1 
#  BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"
# Refer to this graphic for help:
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.85:
  print("underweight")
elif bmi >= 18.5 and bmi < 25:
  print("normal weight")
else:
  print("overweight")
  # case 5 WELCOME TO ROLLARCOASTER 
print("welcome to roller coaster")
height =float(input("enter ur height"))
age = float(input("enter ur age")) 
bill = 0
if height > 180:
 print("Get ready to the entusiasium")
 if age < 12:
   bill += 5
   print("ur ticket is 5$")
 elif age == 12 and age <18:
    bill += 7
    print ("ur tichet is 7$")
 else:
    bill += 12
    print("ur ticket is 12$")
else:
 print("better luch next time")
photo = input(" do u need a photo type s for yes and n for no: ")
if photo == "y":
  bill +=3
  print("your photo")
else :
  print("no photo")
print(F"bill is {bill}") 
 #  CASE WELCOME TO PYTHON PIZZA DELEIVERIES 
print("Welcome to python pizza deliveries")
pizza= input("what kind of pizza do u wanna have s or m or l:")
bill = 0
pepperoni= input("perreroni? y or n")
cheese = input("need a pizza cheesy? y or n")
if cheese == "y":
    bill += 1
if pizza =="s":
    bill += 15
    if pepperoni =="y":
       bill += 2
elif pizza == "m":
    bill += 20
    if pepperoni =="y":
       bill +=3
else :
    bill += 25
if pepperoni =="y":
       bill +=3
print("your bill ",+bill)
  # case 7 
print("welcome to roller coaster")
height =float(input("enter ur height"))
age = float(input("enter ur age")) 
bill = 0
if height > 180:
 print("Get ready to the entusiasium")
 if age < 12:
   bill += 5
   print("ur ticket is 5$")
 elif age == 12 and age <18:
    bill += 7
    print ("ur tichet is 7$")
 elif age > 30 and age < 45:
    bill = 0
    print("u got a free ticket congrats")
 elif age >= 45:
    bill += 12
    print (" ur ticket is 12$")
else:
 print("better luch next time")
photo = input(" do u need a photo type y for yes and n for no: ")
if photo == "y":
  bill +=3
  print("your photo")
else :
  print("no photo")
print(F"bill is {bill}")   


