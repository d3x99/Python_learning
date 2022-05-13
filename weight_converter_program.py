print("Its a weight converter program")
weight = input("Weight: ")
standard = input('(L)bs or (K)g: ')

if standard.upper == 'l':
    lbs_to_kg = float(weight) * 0.45359237
    print(f"You are {round(lbs_to_kg, 1)} kilograms")
elif standard.upper == "k":
    kg_to_lbs = float(weight) * 2.20462262
    print(f"You are {round(kg_to_lbs, 1)} pounds")
else:
    print("You inserted incorrect value")