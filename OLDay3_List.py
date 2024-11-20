# #### Lists ####

# ## How to create? ##
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#         #      0          1        2       3        4          5         6          7

# # How to display things in a list
# which = int(input("Which planet in numbers do you want to know its name? ")) # input allows the user to find which planet they need
# print(planets[which - 1]) # retrieving values from  the list

# # How to change values in a list
# plan = int(input("Which planet to change? "))
# planets[plan - 1] = "Earth 2"
# print(planets)

# # How to add a new value to the back of the list
# planets.append("Pluto")
# print("Pluto is back")
# print(planets)

# # How to add a new value to the list in any position .insert()
# planets.insert(0, 'lalaland')
# print("lalaland added")
# print(planets)

# # How to remove items from a list
# # Deleting (del())
# print("Removing", planets[0])
# del(planets[0])
# print(planets)

# # remove()
# print("Removing Venus")
# planets.remove("Venus")
# print(planets)

# # pop(), removes last item of the list
# print("Bye", planets[-1])
# planets.pop()
# print(planets)

# # len() to check length of a list
# numplanets = len(planets)
# print(f"There are {numplanets} planets in the solar system now.")

# # How to loop through each item in the list
# for i in range(len(planets)):
#     planets[i] = 'New ' + planets[i] # add a 'New' in front of each planet's name
# for p in planets:
#     print("Someday I will visit", p) # display print statements of every planet



'''
2020 - Task 2 [10]
The following program checks it the personal identification number (PIN) 
entered for a locker is correct. There are 10 lockers available and the 
correct PIN for each locker is stored in an array.
A PIN cannot start with the digit 0.

The program allows the user to enter the number of the locker they 
want to open, and a PIN. It checks if the PIN is correct for that locker.
'''
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# locker = int(input("Please enter the locker you would like to open: "))
# pin = float(input("PLease enter the PIN for the locker: "))
# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else: 
#     print("Incorrect PIN for that locker")

'''
1.	Edit the program so that it converts the PIN input 
by the user to an integer.
Save your program
[1] 
'''
# Write and test your code here
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# locker = int(input("Please enter the locker you would like to open: "))
# pin = int(input("PLease enter the PIN for the locker: "))
# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else: 
#     print("Incorrect PIN for that locker")


'''
2.	Edit the program to only accept a locker number between 1 and 10 
(inclusive) to be input. A suitable error message must be displayed 
if the locker number input is not in this range. The program must 
loop until a valid locker number is input.
Save your program.
[3]
'''
# Write and test your code here
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# while True:
#     locker = int(input("Please enter the locker you would like to open: "))
#     if 1 <= locker <= 10:
#         print("Valid locker number")
#         break
#     else:
#         print("Invalid locker number")
# pin = int(input("PLease enter the PIN for the locker: "))
# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else: 
#     print("Incorrect PIN for that locker")

'''
3.	Edit the program to only accept a PIN of 4 digits to be 
entered by the user. A suitable error message must be displayed 
if an incorrect input is given. The program must loop until the PIN 
input is 4 digits.
Save your program
[3]
'''
# Write and test your code here
# while True:
#     locker = int(input("Please enter the locker you would like to open: "))
#     if 1 <= locker <= 10:
#         print("Valid locker number")
#         break
#     else:
#         print("Invalid locker number")
# while True:
#     pin = int(input("PLease enter the PIN for the locker: "))
#     if len(str(pin)) == 4 and str(pin).isdigit:
#         print("Valid locker PIN")
#         break
#     else:
#         print("Invalid locker PIN. PIN must be 4 digits long")
# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else: 
#     print("Incorrect PIN for that locker")

'''
4.	Edit the program to loop until the user inputs both a 
correct locker number and the matching PIN for that locker.
Save your program.
[3]
'''
# Write and test your code here
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]

# while True:
#     while True:
#         locker = int(input("Please enter the locker you would like to open: "))
#         if 1 <= locker <= 10:
#             print("Valid locker number")
#             break
#         else:
#             print("Invalid locker number")
#     while True:
#         pin = int(input("Please enter the PIN for the locker: "))
#         if len(str(pin)) == 4 and str(pin).isdigit:
#             print("Valid locker PIN")
#             break
#         else:
#             print("Invalid locker PIN. PIN must be 4 digits long")
#     if pin == arraypins[locker-1]:
#         print("The locker is open.")
#         break
#     else: 
#         print("Incorrect PIN for that locker")


"""
MOCK Question - Task 3 [10]

The following program manages a list of scores for a competition. 
The scores are stored in a list, 
and the program allows the user to view the scores or add a new score.
"""
# scores = [8, 7, 9, 10, 6]
# choice = int(input("Enter 1 to view scores, or 2 to add a new score: "))
# if choice == 1:
#     print("Scores:", scores)
# elif choice == 2:
#     new_score = int(input("Enter the new score: "))
#     scores.append(new_score)
#     print("Updated scores:", scores)
# else:
#     print("Invalid choice.")

###
"""
1. Modify the program to ensure that only scores between 1 and 10 can be added.
   Display an error message and prompt the user again if the score is invalid.
   Save your program.
   [3]
"""
# Write and test your code here
# scores = [8, 7, 9, 10, 6]
# choice = int(input("Enter 1 to view scores, or 2 to add a new score: "))
# if choice == 1:
#     print("Scores:", scores)
# elif choice == 2:
#     while True:
#         new_score = int(input("Enter the new score: "))
#         if 1 <= new_score <= 10:
#             scores.append(new_score)
#             print("Updated scores:", scores)
#             break
#         else:
#             print("Invalid score, try again")
# else:
#     print("Invalid choice.")

### end question
"""
2. Edit the program to display the number of scores in the list when 
   the user selects to view the scores.
   Save your program.
   [2]
"""
# Write and test your code here
# scores = [8, 7, 9, 10, 6]
# choice = int(input("Enter 1 to view scores, or 2 to add a new score: "))
# if choice == 1:
#     print("Scores:", scores)
# elif choice == 2:
#     while True:
#         new_score = int(input("Enter the new score: "))
#         if 1 <= new_score <= 10:
#             scores.append(new_score)
#             print("Updated scores:", scores)
#             break
#         else:
#             print("Invalid score, try again")
# else:
#     print("Invalid choice.")

###
"""
3. Extend the program to allow the user to remove a specific score from the list.
   The user must enter the exact score they wish to remove.
   If the score is not in the list, display an error message.
   Save your program.
   [3]
"""
# Write and test your code here
# scores = [8, 7, 9, 10, 6]
# choice = int(input("Enter 1 to view scores, or 2 to add a new score: "))
# if choice == 1:
#     print("Scores:", scores)
# elif choice == 2:
#     while True:
#         new_score = int(input("Enter the new score: "))
#         if 1 <= new_score <= 10:
#             scores.append(new_score)
#             print("Updated scores:", scores)
#             break
#         else:
#             print("Invalid score, try again")
# else:
#     print("Invalid choice.")

# delete = int(input("Enter 3 to remove a score? "))
# if delete == 3:
#     while True:
#         what = int(input("Which number to delete? "))
#         if what not in scores:
#             print("Score is not in the list. Invalid number")
#         else:
#             while what in scores:
#                 scores.remove(what)
#             print("Final score: ", scores)
#             break
# else:
#     print("Final score: ", scores)

###
"""
4. Enhance the program to loop until the user chooses to exit.
   Display a menu with options to view scores, add a score, remove a score, or exit.
   Save your program.
   [2]
"""
# Write and test your code here
scores = [8, 7, 9, 10, 6]
while True:
    choice = int(input("Enter 1 to view scores, or 2 to add a new score, or 3 to remove a score (enter exit to exit): "))
    if choice == 'exit':
        print("Final scores: ", scores)
        break
    else:
        if choice == 1:
            print("Scores:", scores)
        elif choice == 2:
            while True:
                new_score = (input("Enter the new score : "))
                if 1 <= new_score <= 10:
                    scores.append(new_score)
                    print("Updated scores:", scores)
                else:
                    print("Invalid score, try again")
        elif choice == 3:
            while True:
                what = int(input("Which number to delete? "))
                if what not in scores:
                    print("Score is not in the list. Invalid number")
                else:
                    while what in scores:
                        scores.remove(what)
                    print("Final score: ", scores)
                    break
        else:
            print("Invalid choice.")
    while True:
        delete = int(input("Enter 1 to view scores, or 2 to add a score, or 3 to remove a score? (Enter exit to exit) "))
        if delete == 'exit':
            print("Final score: ", scores)
            break
        if delete == 1:
            print("Scores:", scores)
        if delete == 3:
            while True:
                what = int(input("Which number to delete? "))
                if what not in scores:
                    print("Score is not in the list. Invalid number")
                else:
                    while what in scores:
                        scores.remove(what)
                    print("Final score: ", scores)
                    break
        elif delete == 2:
            while True:
                new_score = int(input("Enter the new score : "))
                if 1 <= new_score <= 10:
                    scores.append(new_score)
                    print("Updated scores:", scores)
                else:
                    print("Invalid score, try again")
        else:
            print("Final scores: ", scores)