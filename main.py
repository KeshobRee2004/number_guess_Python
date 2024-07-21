#importing modules
import random
import math

# taking input from user 
lower_bound = int(input("Enter the lower bound"))
upper_bound = int(input("Enter the upper bound"))

x = random.randint(lower_bound,upper_bound)#letter I will rename x as random_number


#calculating total no. of chances
total_chances = math.ceil(math.log(upper_bound - lower_bound +1,2))
print(f"you have only {total_chances} chances to guess the number ")

count = 0
flag = False

while count < total_chances:
    count += 1
    guess = int(input("Enter your guess:"))
    if x == guess:
        print("Congratulations you did it in ", count, "try")

    #Once guessed,loop will break
        flag = True
        break
    elif x > guess:
        print("You guessed too low")
    else:
        print("You guessed too high")
if not flag:
    print("The number was",{x})
    print("Better luck next time")