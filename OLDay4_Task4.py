'''
2018 - Task 4 [20]
You have been asked to create a guessing game program.
The program should:
- Allow player 1 to input a whole number between 
1 and 50 inclusive, for player 2 to guess. 

There must be validation present to check that the 
number entered is between 1 and 50 inclusive.

-	Allow player 2 to have 5 guesses to correctly guess 
the number input by player 1. 
You do not need to validate the input for player 2.

-	Output “You guessed the correct number.” 
When player 2 inputs the same number as player 1. 
The game must end if the correct number is guessed.

-	Output “You did not guess the correct number.” 
When player 2 does not input the same number as player 1.

-	Output “Game over!” when player 2 has five incorrect guesses.
'''

'''
10.	Write your program and test that it works.
[10]
'''
# Write and test your code here
# while True:
#     p1num = int(input("Player 1, enter a number between 1 and 50: "))

#     # Validate that p1num is between 1 and 50
#     if p1num >= 1 and p1num <= 50:
#         print("Thank you, Player 1")
#         break
#     else:
#         print("You must enter a number between 1 and 50 only.")
# # Player 2's turn
# for i in range(5):
#     p2guess = int(input("Player 2, guess a number between 1 and 50 (inclusively): "))
#     if p2guess == p1num:
#         print("You guessed the correct number.")
#         break
#     else:
#         print("You did not guess the correct number.")
# else:
#     # loop ended naturally (player 2 ran out of guesses)
#     print("Game over!")


##### END QUESTION
'''
11.	When your program is complete, test it for the following:
a.	Test 1 - Player 1 inputs the number 55
b.	Test 2 - Player 1 inputs the number 0
c.	Test 3 - Player 1 inputs the number 10 and player 2 guesses 
    the numbers 15 and 10
d.	Test 4 - Player 1 inputs the number 20 and player 2 guesses 
    the numbers 30, 35, 22, 15, 49
[4]
'''
# Test Your Code ABOVE



##### END QUESTION
'''
12.	
Extend your program to identify if player 2's 
guess is lower or higher than the number input by player 1. 
A suitable message must then be output.

Save your program.
[2]
'''
# Copy your code from above. Write and test your code here
# while True:
#     p1num = int(input("Player 1, enter a number between 1 and 50: "))

#     # Validate that p1num is between 1 and 50
#     if p1num >= 1 and p1num <= 50:
#         print("Thank you, Player 1")
#         break
#     else:
#         print("You must enter a number between 1 and 50 only.")
# # Player 2's turn
# for i in range(5):
#     p2guess = int(input("Player 2, guess a number between 1 and 50 (inclusively): "))
#     if p2guess == p1num:
#         print("You guessed the correct number.")
#         break
#     elif p2guess > p1num:
#         print("Your guess is higher than player 1's number.")
#     elif p2guess < p1num:
#         print("Your guess is lower than player 1's number.")
#     else:
#         print("You did not guess the correct number.")
# else:
#     # loop ended naturally (player 2 ran out of guesses)
#     print("Game over!")



##### END QUESTION
'''
13.	

Extend your program to allow player 2 to choose an 
easy, medium or hard game. 

An easy game allows eight guesses, a medium game allows 
six guesses and a hard game allows four guesses.

If player 2 inputs a correct guess, the program must output the 
number of guesses made.

You are not required to validate the input for player 2.

Save your program.
[4]
'''
# Copy your code from above. Write and test your code here
# while True:
#     p1num = int(input("Player 1, enter a number between 1 and 50: "))

#     # Validate that p1num is between 1 and 50
#     if p1num >= 1 and p1num <= 50:
#         print("Thank you, Player 1")
#         break
#     else:
#         print("You must enter a number between 1 and 50 only.")
# # Player 2's turn
# while True:
#     level = input("Choose an easy, medium or hard game level: ")
#     if level.lower() == 'easy':
#         n = 8
#         break
#     elif level.lower() == 'medium':
#         n = 6
#         break
#     elif level.lower() == 'hard':
#         n = 4
#         break
#     else:
#         print("Must input hardness level to continue.")

# for i in range(n):
#     p2guess = int(input(f"Player 2, guess a number between 1 and 50 (inclusively). You have {n} guesses left: "))
#     n -= 1
#     if p2guess == p1num:
#         print("You guessed the correct number.")
#         break
#     elif p2guess > p1num:
#         print("Your guess is higher than player 1's number.")
#     elif p2guess < p1num:
#         print("Your guess is lower than player 1's number.")
#     else:
#         print("You did not guess the correct number.")
# else:
#     # loop ended naturally (player 2 ran out of guesses)
#     print("Game over!")


##### END QUESTION

while True:
    p1num = int(input("Player 1, enter a number between 1 and 50: "))

    # Validate that p1num is between 1 and 50
    if p1num >= 1 and p1num <= 50:
        print("Thank you, Player 1")
        break
    else:
        print("You must enter a number between 1 and 50 only.")
# Player 2's turn
while True:
    level = input("Choose an easy, medium or hard game level: ")
    if level.lower() == 'easy':
        n = 8
        break
    elif level.lower() == 'medium':
        n = 6
        break
    elif level.lower() == 'hard':
        n = 4
        break
    else:
        print("Must input hardness level to continue.")

for i in range(n):
    p2guess = int(input(f"Player 2, guess a number between 1 and 50 (inclusively). You have {n} guesses left: "))
    n -= 1
    if p2guess == p1num:
        print("You guessed the correct number.")
        break
    elif p2guess > p1num:
        print("You did not guess the correct number.")
        print("Your guess is higher than player 1's number.")
    elif p2guess < p1num:
        print("You did not guess the correct number.")
        print("Your guess is lower than player 1's number.")
    this = True
    while this == True:
        help = input("Enter 'Y' to get help or 'N' to continue guessing: ")
        if help == 'N':
            print("No help.")
        else:
            if p1num % 2 == 0: # check for remainder
                print("Player 1's number is even")
                this == False
            else:
                print("Player 1's number is odd")
                this == False
            
    

else:
    # loop ended naturally (player 2 ran out of guesses)
    print("Game over!")