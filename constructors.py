class Point:
    def __init__(self, z, v, y):
        self.z = z
        self.v = v
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")



point1 = Point(10, 20, 30)
print(point1.z)
print(point1.v)
print(point1.y)

Point.move(22)