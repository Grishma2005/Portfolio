import random

password = input("Enter your password: ")

if len(password) < 9:
    print("Password too short.")
    exit()

for _ in range(3):
    position = random.randint(1, len(password))
    letter = input(f"Enter letter at position {position}: ")

    if letter != password[position - 1]:
        print("\nSecurity check failed.")
        exit()
    else:
        print("Correct")

print("Security check passed.")
