#### Starting codes ####

# print("Hello, World!")
# print("Hello, my name is Jerrell.\nMy hobby is gaming.")

# x = 10
# y = 20
# equation = x + y
# print(equation)

# hobby = 'gaming'
# print("My hobby is", hobby) # string concatenation

# name = input("Key in your name: ")
# title = input("Key in your title: ")
# print(f"My name is {name}\nI am a {title}\nYou shall know me as {title} {name}")

# math
# num1 = 200
# num2 = 300
# ans = num1 + num2
# print(f"{ans} = {num1} + {num2}")

# my_name = input("Enter your name: ")
# print("Your name is", my_name)

# name1 = input("What's your name? ")
# command = input("What's the command? ")
# print(name1, "commands the people to", command)


#### Variable Types and Type Casting ####

# simple addition
# numb1 = int(input("What is the first number: "))
# numb2 = int(input("What is the second number: "))
# print(numb1 + numb2)

# addition in decimals
# numb1 = float(input("What is the first number: "))
# numb2 = float(input("What is the second number: "))
# print(numb1 + numb2)

# addition in and integer
# numb1 = float(input("What is the first number: "))
# numb2 = float(input("What is the second number: "))
# print(round(numb1 + numb2))

# var1 = "BOB"
# var2 = "DIAMOND"
# var3 = "I AM"
# var4 = var1 + var2
# print(var4)

# var5 = 10
# var6 = 20
# var7 = var5 + var6
# print(var7)

# # Error (cannot put string and integer together)
# var8 = var1 + var5
# print(var8)

# # Correction
# var9 = var1 + str(var5)
# print(var9)

# # Exception
# var10 = var1 * var5
# print(var10)


#### Loops (for and while loop) ####

# for loops
# for i in range(10):
#     print("Hello") # indentation is 4 spaces which tells if the code is part of a loop
#     print("bababa")


# print hello,bye,hello,bye
# for l in range(3):
#     for o in range(3):
#         print("Hello")
#     for p in range(3):
#         print("Bye")
#     print("\n")


### Loop through all values of a string ###

## Cheer Program ##
# name_input = input("Who to cheer for: ")

# for i in name_input: # i stands for "everycharacter in"
#     print("Give me a", i)
#     print(i,"!")

# print("Who is the best?!")
# print(name_input, "!!!!!!")

### for loop to count numbers ###
# for k in range(10):
#     print(k)

# Option 1: range(stop)
# for h in range(10):
#     print(h)

# Option 2: range(start, stop):
# for j in range(1, 11):
#     print(j)

# for g in range(67, 97): # print 67 to 97
#     print(g)

# Option 3: range(start, stop, step)
# for f in range(3, 37, 3):
#     print(i)

# for d in range(6, 73, 6):
#     print(d)

# count down from 15 to 1
# for s in range (15, 0, -1):
#     print(s)

#### Algorithm CHallenge ####
# your_name = input("What is your name? ") # Task 1 (ask for user's name)
# allowance = float(input("How much is your allowance? ")) # Task 2 (ask user for their current weekly allowance)
# yearly_allowance = allowance * 52 # Task 3 (calculate the allowance the user will have in a year)
# total_allowance_received = yearly_allowance * 10 # Task 4 (calculate the allowance in primary and secondary school)
# print(f"{your_name} would have received {total_allowance_received} from primary 1 to secondary 4")


#### Calculate length of person's full name ####
# First and Last name

# fname = input("Enter first name: ")
# lname = input("Enter last name: ")

# calculate how long is the name (len() function)
# total = len(fname) + len(lname)
# print("The total length of", fname, lname, "is", total)


#### Random Number Generator (lottery) ####
import random

# empty list
randnums = [] # To have a list of numbers

while len(randnums) < 6:
    num = random.randint(1, 47)

    if num not in randnums:
        randnums.append(num)

print(randnums)