print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================\n")

prices = []
pizza_number = 1


while len(prices) < 4:
    try:
        price = float(input(f"Enter Price of Pizza #{pizza_number}: "))
        if price <= 0:
            print("Please enter a valid price!")
        else:
            prices.append(price)
            pizza_number += 1
    except ValueError:
        print("Please enter a valid price!")


original_total = sum(prices)
cheapest_pizza = min(prices)
discounted_total = original_total - cheapest_pizza

discount_percentage = (cheapest_pizza / original_total) * 100

print(f"\nOrder Total is £{discounted_total:.2f}, "
      f"a fabulous discount of {discount_percentage:.0f}%!")
