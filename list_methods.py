'''

numbers = [5, 2, 5, 1, 7, 5, 4]

numbers.append(20)
numbers.insert(0, 'lubie placki')
numbers.remove(5)
numbers.pop()


print(numbers)

#numbers.clear()
#print(numbers)

print(numbers.index(5))
print(50 in numbers)
print(numbers.count(5))

numbers = [2, 56654, 12, 345, 564]
numbers.sort()
numbers.reverse()
print(numbers)

numbers_2 = numbers.copy()
'''
# program which remove duplicates in list

list_numbers = [1, 1, 1, 4, 5, 2, 2, 3, 4, 5, 6, 6, 1, 9, 33, 22, 65]
uniques = []
print(list_numbers)

for item in list_numbers:
    if list_numbers.count(item) > 1:
        list_numbers.remove(item)
print(list_numbers)

list_numbers.append(65)
for number in list_numbers:
    if number not in uniques:
        uniques.append(number)
print (uniques)









