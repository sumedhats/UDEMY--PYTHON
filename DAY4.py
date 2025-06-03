# case 1
import random 
random_number = random.randint(1,10)
print(random_number)
# case 2
import trial
print(trial.random_number)
# case 3
import random
randon_num = random.random()
print(randon_num)
random_float = random.uniform(1,10)
print(random_float)
# case 4
random_choice = random.randint(1,2)
if random_choice == 1:
    print("heads")
else:
    print("tails")
    # case 5
    sumi = ["chiru","viki","vinu","abhi","hemi","sachi","ammu","chandu","kavi"]
    print(sumi[0])
    sumi[0] = "chinnu"
    print(sumi[0])
    sumi.append("pappa")
    print (sumi)
    sumi.extend(["rcb","niti"])
    print(sumi)
# case 6
back_stabbers =["chinchu","preethi","deeksha"]
print(random.choice(back_stabbers))
