#Function 
def in_range(n):
    if n >= 0 and n <= 100:
        return True
    else:
        return False

num = int(input("Enter a number: "))
print(in_range(num))

#Upper and Lower Cases
def count_upper_lower(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1

    return upper, lower
s = input("Enter text: ")
u, l = count_upper_lower(s)
print("Uppercase:", u)
print("Lowercase:", l)
 
def greeting():
    g=input("Enter your name:")
    print(f"Hello, {g.lower().capitalize()}!")
greeting()

 #Removing last character
def remove_last_char(s):
    if len(s) <= 1:
        return s
    else:
        return s[:-1]
text = input("Enter a string: ")
print(remove_last_char(text))

#Temperature Conversion
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9
c = float(input("Enter Celsius: "))
print("Fahrenheit:", c_to_f(c))

f = float(input("Enter Fahrenheit: "))
print("Celsius:", f_to_c(f))

#Centigrade to Fahrenheit
temp = input("Enter temperature in C (e.g. 25C): ")

celsius = float(temp[:-1])
fahrenheit = (celsius * 9/5) + 32

print(str(fahrenheit) + "F")

#Reading temperatures and give maximum, minimum and mean temperature
for i in range(6):
    temp = input("Enter temperature in celsius: ")
    value = float(temp[:-1])
    temps.append(value)

maximum = max(temps)
minimum = min(temps)
mean = sum(temps) / len(temps)

print("Max:", maximum, "C")
print("Min:", minimum, "C")
print("Mean:", mean, "C")

 #Show output of Temperatures
temps = []

while True:
    temp = input("Enter temperature (e.g. 20C) or press Enter to stop: ")

    if temp == "":
        break

    value = float(temp[:-1])
    temps.append(value)

if len(temps) == 0:
    print("No temperatures entered.")
else:
    maximum = max(temps)
    minimum = min(temps)
    mean = sum(temps) / len(temps)

    print("Max:", maximum, "C")
    print("Min:", minimum, "C")
    print("Mean:", mean, "C")