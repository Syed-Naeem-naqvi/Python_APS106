# Lec 28

# turtle.done() destroys the canvas and turtle

class Point:

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


p1 = Point()
print(p1.x, p1.y)

p2 = Point()
print(p2)
# Constructor sets x and y to 0
p2.x = 2
p2.y = 3
print(p2.x, p2.y)

p3 = Point(3,4)
print(p3.x, p3.y)


class rectangle():

    def __init__(self, corner, w, h):
        self.bottom_left_corner = corner
        self.width = w
        self.height = h

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        self.bottom_left_corner.x += dx
        self.bottom_left_corner.y += dy


r1 = rectangle(Point(10,5), 100, 50)
print(r1.bottom_left_corner.x)
print(r1.bottom_left_corner.y)
print(r1.width, r1.height)






