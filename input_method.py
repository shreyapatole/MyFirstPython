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


