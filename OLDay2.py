### Times table program ### (times table until 12)

# num = int(input("Enter a number: "))
# for i in range(1, 13):
#     ans = i * num
#     print(f"{num} x {i} = {ans}")


#### Conditions #### (Day 2)

## Password Program ##
# password = 'passme'
# guess = input("Enter the password: ")

# while guess != password:
#     print("Password is incorrect")
#     guess = input("Enter the password: ")

# if guess == password:
#     print("Correct!")
# else:
#     print("Incorrect!")


## If, else, elif ## (Grade checker)

# wa1 = int(input("What is your WA1 score? "))
# wa2 = int(input("What is your WA2 score? "))
# wa3 = int(input("What is your WA3 score? "))
# wa4 = int(input("What is your WA4 score? "))

# overall = wa1 * 0.25 + wa2 * 0.25 + wa3 * 0.25 + wa4 * 0.25
# print(f"Your average score of {overall} is this grade:")

# if overall >= 75:
#     print("A1")
# elif overall >= 70:
#     print("A2")
# elif overall >= 65:
#     print("B3")
# elif overall >= 60:
#     print("B4")
# elif overall >= 55:
#     print("C5")
# elif overall >= 50:
#     print("C6")
# else:
#     print("You have failed.")


## Discount shop ##

# num_pens = int(input("Enter how many pens you want to purchase: "))
# price = 5

# if num_pens >= 100:
#     total = 0.9 * (num_pens * price)
# else:
#     total = num_pens * price
# print(f"Total cost of pens: ${total}")


## Number guesser program ##

# import random

# ran = random.randint(1, 100)
# for i in range(1,8):
#     guess = int(input(f"Enter your number between 1 - 100({8 - i} guesses left): "))
#     if guess > ran:
#         print("Too big")
#     elif guess < ran:
#         print("Too small")
#     else:
#         print("Correct! The number is", ran)
#         break
# else:
#     print("All guesses used up, the answer is", ran)


### Logical operator order ### (And, or, not)
## Monkey zoo ##
# anim1 = input("Enter an animal(1): ")
# anim2 = input("Enter an animal(2): ")
# anim3 = input("Enter an animal(3): ")

# if anim1 == "monkey" or anim2 == "monkey" or anim3 == "monkey":
#     print("Go bananas!")
# else:
#     print("That is a boring zoo.")


### Loops (While) ### (when do not know how many times until condition is met)
## Print out the numbers from 0-9 ##

# for i in range(10):
#     print(i)
# # OR
# count = 0
# while count < 10:
#     print(count)
#     count = count + 1


## Pizza shop ## (keep asking for toppings until user types exit)
# toplist = []

# while True:
#     toppings = input("Enter the toppings you would like on your pizza: ")
#     toplist.append(toppings)
#     # exit scenario
#     if toppings == "exit":
#         print(toplist[0 : len(toplist) - 1], "are your toppings for your pizza.")
#         break
#     else:
#         print("Ok, added", toppings)
    

### Math Quiz ### (Keep asking until the person answers correctly)
# import random

# # Repeat 3 times to ask 3 math questions
# for i in range(3):
#     number1 = random.randint(30, 70)
#     number2 = random.randint(30, 70)

#     while True:
#         # ask the question
#         anss = int(input("What is {} + {}? ".format(number1, number2)))
#         if anss == number1 + number2:
#             print("Correct! Answer is", number1 + number2)
#             break # break out of the loop
#         else:
#             print("Answer is wrong!")
# else:
#     print("3/3, Nice!")


### Input validation ###
# Length check, range check, presense check, format check

## Length check ## (Only 4 characters long)
# while True:
#     otp = input("Enter the OTP: ")
#     if len(otp) != 4: # reject otp which doenst have 4 digits
#         print("OTP must only be 4 digits. Try again.")
#     else:
#         print("OTP accepted")
#         break

##################################################################################
'''
Question 3 (Range Check):
Write the input entry and validation code for a program 
that needs to accept a secondary student's age.

The age must be between 13 and 16 inclusive.

If the input is invalid, your code should keep trying 
by asking for the input to be entered again.

Sample output:
Enter age: 12
Invalid input. Age must be between 13 and 16.
Enter age: 20
Invalid input. Age must be between 13 and 16.
Enter age: 16
Age accepted.
'''
# Question 3 answer (range check) #
# while True:
#     age = int(input("Enter your age: "))
#     if 13 <= age <= 16:
#         print("Age accepted.")
#         break
#     else:
#         print("Invalid input. Age must be between 13 and 16.")


## Format check ##
# while True:
#     user = input("Enter username: ")
#     if user.islower() == False:
#         print("Invalid input. Username must be in lowercase.")
#     else:
#         print("Username accepted.")
#         print("Hello,", user, "!")
#         break

