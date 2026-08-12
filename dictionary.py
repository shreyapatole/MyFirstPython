person = {
    "first_name" : "shreya",
    "last_name" : "patole",
    "age" : 19,
    "city" : "pune",
}
print(person)

favorite_numbers = {
    "shreya" : 3,
    "devyani" : 6,
    "piu" : 4, 
    "sam" : 1,
    "om" : 2,
}
print(favorite_numbers)

word_meaning = {
    "print" : "method used to print messages on the terminal.",
    "for" : "a loop",
    "list" : "sequence of values within square brackets that can be changed.",
    "tuples" : "sequence of values within parenthesis that are immutable.",
    "dictionary" : "used to store data in key-value pairs."
}

for key in word_meaning :
    print(f"\n{key.lower()} : \n\t{word_meaning.get(key,"No value assigned").title()}")
print() #For a extra blank line


# Another way to loop through dictionary :
for word, meaning in word_meaning.items() :
    print(f"\n{word.lower()} : \n\t{meaning}")
print()
list1 = word_meaning.items()
for item in list1 :
    print(item)


rivers_city = {
    "Krishna" : "Sangli",
    "Panch Ganga" : "Kolhapur",
    "Ganga" : "Delhi"
}

for river, city in rivers_city.items() :
    print(f"The {river.title()} runs through {city.title()}")

print("\nFollowing are the rivers mentioned in the list :")
for river in rivers_city.keys() :
    print(f"\t{river.title()}")

print("\nFollowing are the cities mentioned in the list :")
for city in rivers_city.values() :
    print(f"\t{city.title()}")


people = ["shreya", "srushti", "sejal", "devyani", "piu", "samarth", "omkar"]
favorite_language = {
    "shreya" : "python",
    "devyani" : "java",
    "piu" : "ruby",
}

for person in people :
    if person not in list(favorite_language.keys()) :
        print(f"Hi {person}, Please take the poll.")
    else :
        print(f"Hi {person}, Thankyou for taking the poll.")


person1 = {
    "first_name" : "shreya",
    "last_name" : "patole",
    "class" : "TE",
    "age" : 19,
    "city" : "pune",
    "skills" : ["Python", "Java"]
}
person2 = {
    "first_name" : "devyani",
    "last_name" : "patole",
    "class" : "FE",
    "age" : 18,
    "city" : "Kolhapur",
}
person3 = {
    "first_name" : "Piu",
    "last_name" : "patole",
    "class" : "10th",
    "age" : 16,
    "city" : "Kolhapur",
}

people_list = [person1, person2, person3] 
for person in people_list :
    
    
    print(f"Full name : {person['first_name'].title()} {person['last_name'].title()}")
    print(f"Age : {person['age']}")
    print(f"Class : {person['class']}")
    print(f"City : {person['city'].title()}")
    if 'skills' in person.keys():
        print("Skills are :")
        for skill in person['skills'] :
            print(f"{skill.title()}", end = " ")
        print()
    print()


cat = {
    "kind" : "persian",
    "owner" : "samarth",
}

dog = {
    "kind" : "bulldog",
    "owner" : "omkar",
}

parrot = {
    "kind" : "west-asian",
    "owner" : "shreya",
}

pets = [cat, dog, parrot]

for pet in pets :
    print(f"Kind of animal is {pet['kind'].title()} which is owned by {pet['owner'].title()}.")


favorite_places = {
    "shreya" : ["japan", "new york", "eisenburg"],
    "devyani" : ["japan", "korea", "china"],
    "piu" : ["korea", "china"],
    "srushti" : ["korea"]
}

for person, places in favorite_places.items() :
    if len(places) > 1 :
        print(f"{person.title()}'s favorite places are :")
        for place in places :
            print(f"\t{place.title()}")
        
    elif len(places) == 1 :
        print(f"{person.title()}'s favorite place is {places[0].title()}")
    print()


favorite_numbers = {
    "shreya" : [1,2,3],
    "devyani" : [6,5],
    "piu" : [4,7],
    "patole" : [1]
}

for person, numbers in favorite_numbers.items() :
    if len(numbers) > 1 :
        print(f"{person.title()}'s favorite numbers are :", end = " ")
        for number in numbers :
            print(f"{number}", end = " ")
        print()

    elif len(numbers) == 1:
        print(f"{person.title()}'s favorite number is {numbers[0]}.")


cities = {
    "tokyo" : {
        "country" : "japan",
        "population" : 10000,
        "fact" : "It is the capital of Japan",
    },

    "mumbai" : {
        "country" : "india",
        "population" : 100000,
        "fact" : "It is the busiest city in the Maharashtra",
    },

    "seoul" : {
        "country" : "south korea",
        "population" : 50000,
        "fact" : "It is the capital of South Korea",
    },
}

for city, city_info in cities.items() :
    print(f"{city.title()}'s information is as below :")
    print(f"\tLocated in {city_info['country'].title()}.")
    print(f"\tPopulation is around {city_info['population']}.")
    print(f"\tFact about {city.title()} : {city_info['fact']}.")
    print()

# Creating a dictionary with frequency of each element in list :
dict1 = {}
words = ["python", "java", "python", "c", "java", "python"]
for word in words :
    if word in dict1.keys() :
        dict1[word] += 1
    else :
        dict1[word] = 1
print(dict1)