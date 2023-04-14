import time

import names
# print(names.get_first_name("female"));

# print("Hello World Wazzup")
# print("Day 1 - Python print Function\n"
#       "The function is delcared like this\n"
#       "print('what to print'")
#
#
# print('Hello World')

# print("Hello World\n"
#       "My name is Nigga man")
#
# print("Hello" + " World")

#
# name = input("What is your name?")
#
# print(f"Your name is {len(name)} words long")


# name = input("What is your name")
# name_length = len(name)
# print(name_length)

# a = input("a: ")
# b = input("b: ")
#
# print("Switching")
# time.sleep(2)
#
# temp = a
# a = b
# b = temp
# print(f"a: {a}")
# print(f"b: {b}")


print("Welcome to the pet NameInator")
time.sleep(1)

gender = str.lower(input("What is the pet gender? (male or female)\n"))

if gender == "male":
    print("Your pet should be called " + names.get_first_name(gender))
elif gender == "female":
    print("Your pet should be called " + names.get_first_name(gender))
