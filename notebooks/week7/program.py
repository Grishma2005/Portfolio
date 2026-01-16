# sorted Letters
def unique_letters_sorted(text: str) -> list[str]:
    return sorted(set(text))

# tests
print(unique_letters_sorted("cheese"))   
print(unique_letters_sorted("Hello"))   

# Set operations
def letters_in_at_least_one(a: str, b: str) -> list[str]:
    return sorted(set(a) | set(b))

def letters_in_both(a: str, b: str) -> list[str]:
    return sorted(set(a) & set(b))

def letters_in_either_not_both(a: str, b: str) -> list[str]:
    return sorted(set(a) ^ set(b))

# tests
print(letters_in_at_least_one("cheese", "bread"))
print(letters_in_both("cheese", "bread"))
print(letters_in_either_not_both("cheese", "bread"))

# Countries and capitals
def normalise_country(name: str) -> str:
    return name.strip().lower()

capitals = {}  

while True:
    country = input("Enter a country (or 'quit' to stop): ").strip()
    if country.lower() == "quit":
        print("Goodbye!")
        break

    key = normalise_country(country)
    if key in capitals:
        print(f"The capital of {country} is {capitals[key]}.")
    else:
        capital = input(f"I don't know the capital of {country}. Please enter it: ").strip()
        if capital:
            capitals[key] = capital
            print("Saved!")
        else:
            print("No capital entered, not saved.")

# Frequency
def top_six_letters(message: str) -> list[tuple[str, int]]:
    counts = {}

    for ch in message.lower():
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1


    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:6]


msg = "Hello there! Here we have some letters... EEEEE!!!"
top6 = top_six_letters(msg)
print(top6)


for letter, count in top6:
    print(letter, "->", count)