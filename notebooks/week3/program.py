#Greeting
name = input("Hello, what is your name? ")

if name == "":
    print("Hello, Stranger!")
else:
    print(f"Hello, {name}!")


# Reset password
p1 = input("Enter a new password: ")
p2 = input("Enter it again: ")

if p1 != p2:
    print("Error:Password doesnot match.")
elif 8 >len(p1) or 12> len(p1):
    print("Error: password must be 8 to 12 characters long.")
else:
    print("Password set.")
# Table of seven
for x in range(0,13):
    print(f"{x} X 7 = {x*7}")
# multiply 
table = int(input("Which times table (0 to 12)? "))

if 0 <= table <= 12:
    for i in range(13):
        print(f"{i} x {table} = {i * table}")
else:
    print("Error: please enter a number from 0 to 12.")

 Multiplication table
table = int(input("Which times table (-12 to 12)? "))

if -12 <= table <= 12:
    if table < 0:
        t = abs(table)
        for i in range(12, -1, -1):   # 12 down to 0
            print(f"{i} x {t} = {i * t}")
    else:
        for i in range(13):          # 0 up to 12
            print(f"{i} x {table} = {i * table}")
else:
    print("Error: please enter a number from -12 to 12.")

