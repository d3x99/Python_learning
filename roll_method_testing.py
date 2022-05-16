import random
list1 = []


for x in range(0, 1000000):
    y = random.randint(0, 2)
    list1.append(y)


print(list1.count(0))
print(list1.count(1))
print(list1.count(2))



