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