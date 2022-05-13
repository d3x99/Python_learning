import math

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Maria']
names[0] = 'Jon'
print(names)
print(names[0])
print(names[-1])
print(names[2:])
print(names[:])

numbers = [123333, 155222222222, 2, 65456, 76, 234, 569999999]
biggest_number = 0

for number in numbers:
    if number > biggest_number:
        biggest_number = number
print(biggest_number)

