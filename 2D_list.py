matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
x = matrix[0]
y = matrix[0][0]
print(x)
print(y)

for row in matrix:
    for item in row:
        print(item)