# rental_car = input("What kind of car would you like? ")
# print(f"Let me check if I can find a {rental_car.title()}.")

# group_length = int(input("Enter the number of people in your group : "))
# if group_length > 8 :
#     print("Sorry for the inconvenience, but you'll have to wait for the table.")
# elif group_length > 0 and group_length <= 8 :
#     print("Your table is ready. Enjoy your meal.")

message = "To check whether a number is multiple of 10 or not."
message += "\nEnter a number"
number = int(input(message + " : "))
if number % 10 == 0 :
    print(f"{number} is a multiple of 10.")
else :
    print(f"{number} is not a multiple of 10.")