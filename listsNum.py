for n in range(1,21) :
    print(n)

numbers = list(range(1,100000))
for number in numbers :
    print(number)
print(f"Minimum from the list : {min(numbers)}")
print(f"Maximum from the list : {max(numbers)}")
print(f"Sum of all numbers : {sum(numbers)}")

odd_numbers = list(range(1,20,2))
for num in odd_numbers :
    print(num)

multiples = []
for i in range(1,11) :
    multiples.append(i*3)

print(f"Multiples of 3 from 1 - 10 : {multiples}")


# cubes
cubes = []
for i in range(1,11) :
    cubes.append(i ** 3)

for cube in cubes :
    print(cube)


# generating cubes using list comprehension
cubes2 = [num ** 3 for num in range(1,11)]
print(f"Cubes using list comprehension : {cubes2}")

cities = ["New York", "Tokyo", "Singapore", "London", "Paris", "Berlin", "Sydney", "Dubai", "Hong Kong", "Los Angeles"]

print(f"First three cities in the list : {cities[:3]}")
print(f"Cities in the middle of the list are : {cities[3:7]}")
print(f"Last three cities in the list : {cities[-3:]}")

myFavFood = ["Pani puri", "Biryani", "Mutton"]
friendFavFood = myFavFood[:]

myFavFood.append("Bread Omllete")
friendFavFood.append("Chhole Bhature")

print("My favorite foods are :")
for food in myFavFood :
    print(food)

print("\n\n")
print("My friend's favorite foods are : ")
for food in friendFavFood :
    print(food)
