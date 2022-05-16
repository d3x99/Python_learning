class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.z = 20
point2 = Point()
print(point1.z)
print(point2.draw())