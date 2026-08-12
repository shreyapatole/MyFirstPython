rental_car = input("What kind of car would you like? ")
print(f"Let me check if I can find a {rental_car.title()}.")

group_length = int(input("Enter the number of people in your group : "))
if group_length > 8 :
    print("Sorry for the inconvenience, but you'll have to wait for the table.")
elif group_length > 0 and group_length <= 8 :
    print("Your table is ready. Enjoy your meal.")

message = "To check whether a number is multiple of 10 or not."
message += "\nEnter a number"
number = int(input(message + " : "))
if number % 10 == 0 :
    print(f"{number} is a multiple of 10.")
else :
    print(f"{number} is not a multiple of 10.")

toppings = []
while True :
    topping = input("Enter the topping you wish to add.")
    if topping.lower() == 'quit' :
        break
    toppings.append(topping)
for topping in toppings :
    print(topping)

age = int(input("Enter your age to know the ticket price : "))
ticket_price = "Free"
if age >= 3 and age <= 12 :
    ticket_price = "$10"
elif age > 12 :
    ticket_price = "$15"
print(f"Ticket price is {ticket_price}")

cities = []
active = True
while active :
    city = input("Enter a city you want to visit \nAlso if you wish to quit enter 'quit' : ")
    if city.lower() == 'quit' :
        break
    else :
        cities.append(city.title())
        print(f"{city.title()} added to the list.")
        ans = input("Do you want to continue? yes or no : ")
        if ans.lower() == 'no' :
            active = False

print("Following are the cities you mentioned : ", end = "")
for city in cities :
    print(f"{city} ", end = "")


sandwich_order = ["Veg", "pastrami", "Chicken", "pastrami", "Cheese", "pastrami", "Paneer"]
finished_order = []

print("Sorry for the inconvenience, but we are out of 'Pastrami'.")
while 'pastrami' in sandwich_order :
    sandwich_order.remove('pastrami')

# All the elements in the list will be popped from the end of the list.
while sandwich_order :
    sandwich = sandwich_order.pop()
    print(f"Your order about {sandwich.title()} is ready.")
    finished_order.append(sandwich.title())

# Inserting the elements in same order as in the sandwich_order list.
# Initialised a variable to position 0, so that element at 0th position will be popped out 
# And the rest of the elements will be shifted. This continues until the list 'sandwich_order' is empty.
position = 0
while sandwich_order :
    sandwich = sandwich_order.pop(position)
    print(f"Your order about {sandwich.title()} is ready.")
    finished_order.append(sandwich.title())

for sandwich in finished_order :
    print(f"{sandwich} has been made and served.")


print("User poll about thier dream vacation : ")
dream_vacation = {}
status = True
while status :
    username = input("Please enter your name : ")
    place = input("Enter your dream vacation : ")
    dream_vacation[username] = place

    ans = input("Is anyone interested in taking poll ? (Hint : Answer in yes / no) \n")
    status = False if ans.lower() == 'no' else True

for name, place in dream_vacation.items() :
    print(f"{name.title()}'s dream location is {place.title()}")



numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
numbers_modified = []
for n in numbers :
    if n not in set(numbers_modified) :
        numbers_modified.append(n)
print(numbers)
print(numbers_modified)