birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))
print("You have " + str(age) + " years old")
str(age)
print("now age is a " + str(type(age)))

weight_pounds = input('Your weight in pounds: ')
weight_kg = int(weight_pounds) * 0.45359237
weight_kg_rounded = round(weight_kg, 1)
print("your weight in killograms is " + str(weight_kg_rounded))