#Program 1: Introduction
name = input("Hello, what is your name? ")
print(f"Hello, {name}. Good to meet you!")
 
#program 2: Temperature
celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}C is equivalent to {fahrenheit}F.")

#Program 3: group
students = int(input("How many students? "))
group_size = int(input("Required group size? "))

groups = students // group_size
leftover = students % group_size

print(f"There will be {groups} groups with {leftover} left over.")

 #Program 4: Sweets
sweets = int(input("How many sweets are in the tub? "))
pupils = int(input("How many pupils are there today? "))

each = sweets // pupils
leftover = sweets % pupils

print(f"Give each pupil {each} sweets.")
print(f"There will be {leftover} sweets left over.")
