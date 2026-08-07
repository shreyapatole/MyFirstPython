age = 19
print("age == 18? I predict it's False")
print(age==18)
print("age == 19? I predict it's True")
print(age == 19)

print("Is age between 18 - 25")
print(age > 18 and age < 25)
print("Is age valid?")
print(age > 0 and age < 80)

cars = ["Toyota", "Honda", "bmw", "Chevrolet", "Nissan"]
for car in cars :
    if car == "bmw" :
        print(car.upper())
    else :
        print(car.title())


orders = ["burger", "pizza", "pasta", "soup"]
for order in orders :
    if order=="soup" :
        print("Sorry, no soup available for today!")
    else :
        print(f"Order placed successfully for {order}")

year = "SE"
if year != "FE" :
    print("Sorry to inform, you're not eligible for the program")

numbers = [1, 2, 3, 4, 5]
if 5 in numbers :
    print("5 is present in the list")

if 6 not in numbers :
    print("6 is not present in the list")


alien_color = "green"
if alien_color.lower() == "blue" :
    print("Yahoo!! You just earned 5 points.")
elif alien_color.lower() == "green" :
    print("Yayy! You earned 10 points!")

elif alien_color.lower() == "red" :
    print("Alien is dead. Restart the game?")


age = 1
if age < 2 :
    print("The person is a baby.")
elif age >= 2 and age < 4 :
    print("The person is a toddler.")
elif age >= 4 and age < 13 :
    print("The person is a kid")
elif age >= 13 and age < 20 :
    print("The person is a teenager")
elif age >= 20 and age < 65 :
    print("The person is an adult")
elif age >= 65  and age < 100 :
    print("The person is an elder")



fav_fruits = ["Watermelon", "Grapes", "Pineapple"]
if "Banana" in fav_fruits :
    print("One of your favorites includes banana.")
if "Mango" in fav_fruits :
    print("One of your favorites includes Mango.")
if "Melon" in fav_fruits :
    print("One of your favorites includes Melon.")
if "Grapes" in fav_fruits :
    print("One of your favorites includes Grapes.")
if "Pineapple" in fav_fruits :
    print("One of your favorites includes Pineapple.")



# Working with lists and if stmnts
users = ["admin", "shreya", "devyani", "piu", "omkar"]
if users :
    for user in users :
        if user.lower() == "admin" :
            print(f"Hello {user.title()}, would you like to see the status report?")
        else :
            print(f"Hello {user.title()}, check out the latest updates in your account.")
else :
    print("No users found!")

current_usernames_org = ["shreya", "devyani", "PIU", "omkar", "Samarth"]
current_usernames = []
if current_usernames_org :
    for user in current_usernames_org :
        current_usernames.append(user.lower())
else :
    print("List of current usernames is empty!")

new_usernames = ["shreya", "srushti", "rutuja", "piu", "Sejal"]
if new_usernames and current_usernames :
    for new_username in new_usernames :
        if new_username in current_usernames :
            print(f"Username {new_username.lower()} not available, try a new one.")
        else :
            print(f"Username {new_username.lower()} is available, press 'Enter' to confirm.")
else :
    print("Check if one of the list is empty.")


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, "s")
if numbers :
    for number in numbers :
        if number == 1 :
            print(f"{number}st")
        elif number == 2 :
            print(f"{number}nd")
        elif number == 3 :
            print(f"{number}rd")
        elif isinstance(number,int) :
            print(f"{number}th")
        else :
            print("Not an integer.")