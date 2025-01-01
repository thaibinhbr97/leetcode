class Point:

    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def move_up(self, offset):
        self.y = self.y + offset


one = Point(4, 10)
two = one.move_up(20)
print(one)
print(two)
