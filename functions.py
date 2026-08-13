def display_message() :
    print("I'm learning functions in python, wish me luck!")

display_message()

def favorite_book(bookName, authorName) :
    print(f"One of my favorite book is '{bookName.title()}' written by {authorName.title()}")

favorite_book("To all the boys I've loved before", "jenny han")

def make_shirt(size = "l", text = "i love python") :
    print(f"\nShirt details : \nSize : {size.upper()}, Text that will be printed : '{text.upper()}'")
    print("Thanks for ordering, happy shopping^^")

make_shirt()
snake_bytes = b'\xf0\x9f\x90\x8d'
# print(snake_bytes.decode('utf-8'))
make_shirt("s")
make_shirt(size = "m", text = "all my frnds are" + snake_bytes.decode('utf-8'))
make_shirt(text = "too cool to give a fu*k", size = "L")

def describe_city(name, city = "tokyo") :  
    print(f"{name.title()}'s dream city is {city.title()}.")

describe_city("shreya")
describe_city(name = "devyani", city = "seoul")
describe_city(city = "shibul", name = "piu")