## Phone number checker ##

# while True:
#     phone = (input("Enter mobile number: "))
#     if phone.startswith('8'):
#         print("Mobile number accpeted.")
#         break
#     elif phone.startswith('9'):
#         print("Mobile number accpeted.")
#         break
#     else:
#         print("Invalid input. Mobile number must start with '8' or '9'.")
        # phone = (input("Enter mobile number: "))

## Email checker ##

# while True:
#     email = input("Enter email: ")
#     if email.endswith('.sg'):
#         print("Email accepted.")
#         break
#     else:
#         print("Invalid input. Email must end with '.sg'.")


################################# Dictionary #########################################
### How to define a dictionary ###
shop_price = {'hamburger': 7.5, 'pasta': 15, 'pizza': 25, 'lasagne': 30}

### How to retrieve the value of an item ###
print("$",shop_price["hamburger"])

### How to change the value of an item ###
shop_price['hamburger'] = 10
print("$",shop_price["hamburger"])

### How to add a new key/value to the dictionary ###
shop_price['spaghetti'] = 18
print(shop_price)

### How to delete a key/value from a dictionary ###
del(shop_price['hamburger'])
print(shop_price)

### Loop through all the keys in the dictionary ###
for item in shop_price:
    print(item)

### Scenario: Customer come to the shop, and you ask what they want to buy. 
# Check if customer's choice is in the dictionary
# if yes, tell them the price
# or else, tell them the shop doesn't serve their choice
item_ordered = []
budget = int(input("May I know what is your budget? "))
total = 0

while True:
    choice = input("Enter what would you like (Enter no to exit): ")
    if choice in shop_price:
        print("Yes I sell", choice)
        print("It will be $",shop_price[(choice)])
        budget = budget - shop_price[(choice)]
        total = total + shop_price[(choice)]
        if budget < 0:
            print("You have not enough money, go away")
            break
        else:
            item_ordered.append(choice)
            print(f"You have ${budget} left.")
    elif choice == "":
        print("Hurry up and tell me!")
    elif choice == 'no':
        print(f"You have ${budget} left.")
        break
    else:
        print("Sorry, I don't sell", choice)

# loop through all the items in list to tell customer
print(item_ordered, "are your orders. Total of $", total)
