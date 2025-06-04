# case1 
love = ["viki" , "abhi" , "hemi" , "nithi" ]
for love in love:
    print(love)
# case2
love = ["viki" , "abhi" , "hemi" , "nithi" ]
print(love)
for love in love:
    print(love +"as")
    print(love)
# case3
score = [12,3,3,4,4,6,654,65,6,5465,65,65,65,5,3,4,3,5,43,344,54,43,42]
print(sum(score))
# case4
score = [12,3,3,4,4,6,654,65,6,5465,65,65,65,5,3,4,3,5,43,344,54,43,42]
sum = 0
max = 0
for score in score:
    sum += score
print(sum)
# case 5
score = [12,3,3,4,4,6,654,65,6,565,65,65,65,5,3,4,3,5,43,344,54,43,42]
max = 0 
for score in score:
    if score >max:
        max = score
        print(max)
# case 6
    for num in range(1,10,):
        print(num)
        #case 7
        for number in range(1,101):
            print(number)
      # case 8
total = 0
for number in range(1,101):
    total += number
    print(total)
# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

# Your program should print each number from 1 to 100 in turn and include number 100.

# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
for number in range(1,101):
    if number % 3 ==0 and number%5 ==0:
        print("FizzBuzz")
    elif number % 3 == 0:
         print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
            
            