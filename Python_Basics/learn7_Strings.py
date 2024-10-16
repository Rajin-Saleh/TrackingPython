# #  Learning Strings in Python
# #  Strings,  Stings slicing & operation, string methods


name = "Harry"
friend = "James"
newFriend = 'Bony'

chat = ''' Yo chat!
Hot as fudge'''
print(chat)

print(f"Your name is {name}")

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) this throws an array

print("\nlets use a for loop\n")

for character in chat:
        print(character)   



#   String Slicing

fruit = "mango"
mangoLen = len(fruit) # len to get number of character
print(mangoLen)
print(fruit[1:5]) # including 1 but not 5
print(fruit[:])
print(fruit[0:-3])
print(fruit[-3:-1])
print(fruit[-3:-1])

# Quick Quiz:

nm = "Harry"
print(nm[-4:-2]) # The output is ar


#  String methods

print("\nRecord of upper case name\n")

name3 = input("Put you name in lowercase: ").upper() # upper() makes all the word uppercase letter
print(f"Your name in upper is : {name3}")
print(name3.split(" "))
print(name3)

name4 = input("Put you name in uppercase: ").lower() # lower() makes all the word lowercase letter
print(f"Your name in lower is : {name4}")

name5 = input("Put you name in capitalize: ").capitalize() # capitalize makes the first letter capital 
print(f"Your name in upper is : {name5}")
print(name5.center(50))
print(name5.count('o'))
print(name5.endswith("ood"))


str1 = "His name is Robert. He is a gamer."
print(str1.find("Robert"))
print(str1.title())

name1 = input("What is your name? ").title()
print(f"Your name is {name1}")




