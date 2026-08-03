# 2 LISTS
# names = ["Shreya", "Devyani", "Samarth", "Priyadarshani", "Omkar"]
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])

# print(f"Hello {names[0].title()}")
# print(f"Hello {names[1].title()}")
# print(f"Hello {names[2].title()}")
# print(f"Hello {names[3].title()}")
# print(f"Hello {names[4].title()}")

# countries = ["India", "Japan", "South Korea", "new york"]
# print(f"I want to leave {countries[0].title()}.")
# print(f"And then settle in {countries[1].title()} for good.")
# print(f"After getting a job(s) in {countries[1].title()}, I will travel to {countries[2].title()}.")
# print(f"I will also explore {countries[3].title()} bcoz it is very cool!!")

# invitor = "Shreya"
# guest_list = ["Anuja", "Devyani", "Piu"]
# print(f"Hello {guest_list[0]}!, You are invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")
# print(f"Hello {guest_list[1]}!, You are invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")
# print(f"Hello {guest_list[2]}!, You are invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")

# print(F"We won't be having {guest_list[0]}")
# guest_list[0] = "Sam"

# print("Modified guest list :")
# print(f"Hello {guest_list[0]}!, You are invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")
# print(f"Hello {guest_list[1]}!, You are invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")
# print(f"Hello {guest_list[2]}!, You are invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")


# print("Guyzz I'm excited to sure that I just found a bigger table, which ofc menas more guests coming. OMG!!")
# guest_list.insert(0,"Omkar")
# guest_list.insert(2,"Srushti")
# guest_list.append("Priyadarshani")
# print(f"Hello {guest_list[0]}!, You are invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")
# print(f"Hello {guest_list[1]}!, You are invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")
# print(f"Hello {guest_list[2]}!, You are invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")
# print(f"Hello {guest_list[3]}!, You are invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")
# print(f"Hello {guest_list[4]}!, You are invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")
# print(f"Hello {guest_list[5]}!, You are invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")


# print("Since the table won't be arriving till dinner the guest list is to be shortened:(")
# removed_guest = guest_list.pop()
# print(f"We're sorry {removed_guest}. Maybe next time!")
# removed_guest = guest_list.pop()
# print(f"We're sorry {removed_guest}. Maybe next time!")
# removed_guest = guest_list.pop()
# print(f"We're sorry {removed_guest}. Maybe next time!")
# removed_guest = guest_list.pop()
# print(f"We're sorry {removed_guest}. Maybe next time!")

# print(f"Hello {guest_list[0]}!, You are still invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")
# print(f"Hello {guest_list[1]}!, You are still invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")


# print(guest_list)
# del guest_list[0]
# print(guest_list)
# del guest_list[0]
# print(guest_list)

# print(f"Hello {guest_list[0]}!, You are still invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")
# print(f"Hello {guest_list[1]}!, You are still invited to attend Ms.{invitor}'s Party. See you at 8pm on Sunday! byeee")
# print(guest_list)
# del guest_list[0]
# print(guest_list)
# del guest_list[0]
# print(guest_list)


favPlaces = ["Japan", "New York", "South Korea", "USA", "Singapore"]
print(f"The original list of favorite places : {favPlaces}")
# print(f"Sorted list using sorted() method : {sorted(favPlaces)}")
# print(f"The original list again : {favPlaces}")
# print(f"Reversed list using sorted method : {sorted(favPlaces, reverse = True)}")
# print(f"The original list again : {favPlaces}")
favPlaces.reverse()
print(f"Reversed list using reverse method : {favPlaces}")
favPlaces.reverse()
print(f"Obtaining original list using reverse() method : {favPlaces}")

favPlaces.sort()
print(f"Sorted list using sort() method : {favPlaces}")
favPlaces.reverse()
print(f"List in reversed alphabetical order : {favPlaces}")