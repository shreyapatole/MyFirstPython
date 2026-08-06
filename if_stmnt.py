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