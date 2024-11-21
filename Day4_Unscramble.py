# WORD UNSCRAMBLE CODE
import random
shuf = 0
words = [
    "python", "computer", "education", "coding", "programming", 
    "algorithm", "debugging", "variable", "function", "software",
    "hardware", "keyboard", "internet", "database", "network", 
    "browser", "website", "developer", "compiler", "iteration", 
    "condition", "looping", "syntax", "recursion", "automation", 
    "simulation", "encryption", "framework", "datascience", "interface"
]
# choose a word randomly
num = random.randint(1, 30)
word = words[num]

#split this into characters in a list
alpha_list = []
for letters in word:
    alpha_list += letters

# shuffle the items in a list
random.shuffle((alpha_list))

# put the list back into a string
scrambled = ''
for c in alpha_list:
    scrambled += c + " "
print(scrambled)

# while true
while True:
    #display the word
    print("Your word to guess is ",scrambled)

    # options Type 1 to scramble again, 2 to guess, 3 to give up:
    option = int(input(f"Type 1 to scramble again, 2 to guess, 3 to give up (You have {5 - shuf} shuffles left): "))

    # if option 1
    if option == 1:
        if shuf <= 4:
            shuf += 1
            random.shuffle((alpha_list))
            scrambled = ''
            for c in alpha_list:
                scrambled += c + " "
        else:
            print("You have used up all your scrambles")
            print(f"Use         {scrambled}          to guess")
            choice = int(input(f"Type 2 to guess, 3 to give up (You have no shuffles left): "))
            guess = input("Enter your guess here: ")
            if guess == word:
                print("Answer is", word)
                print("Congrats, you got it correct!")
                break
            elif option == 3:
                print("Answer is", word)
                print("Sorry, you lost")
                break
            elif option == '':
                print("Must have an answer")
            else:
                print(guess, "is wrong, try again.")

    # elif option 2
    elif option == 2:
        guess = input("Enter your guess here: ")
        if guess == word:
            print("Answer is", word)
            print("Congrats, you got it correct!")
            break
        else:
            print(guess, "is wrong, try again.")
    
    # elif option 3
    elif option == 3:
        print("Answer is", word)
        print("Sorry, you lost")
        break

    # # else Invalid:
    else:
        print("Must have an answer")
