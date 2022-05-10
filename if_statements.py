import math
is_hot = True
is_cold = True


"""
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")
"""

house_price = 1000000
buyer_has_good_credit = True
if buyer_has_good_credit:
    down_payment = 0.1 * house_price
    print(f"Down payment ${down_payment}")
    print(f"Your house is worth ${house_price - down_payment}")

else:
    down_payment = 0.2 * house_price
    print(f"Down payment ${down_payment}")
    print(f"Your house is worth ${house_price - down_payment}")




