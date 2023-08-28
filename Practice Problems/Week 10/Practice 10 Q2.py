import math
import random


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def distance_from_origin(self):
        distance = (self.x**2+self.y**2)**0.5
        return round(distance, 3)


class Square:

    def __init__(self, bottom_left_x=0, bottom_left_y=0, top_right_x=0, top_right_y=0):
        self.bottom_left = Point(bottom_left_x, bottom_left_y)
        self.top_right = Point(top_right_x, top_right_y)

    def __str__(self):
        return '(' + str(self.bottom_left) + ',' + str(self.top_right) + ')'

    def calculate_area(self):
        dx = self.top_right.x - self.bottom_left.x
        dy = self.top_right.y - self.bottom_left.y
        return dx * dy


class Circle:
    def __init__(self, center_x=0, center_y=0, radius=0):
        self.center = Point(center_x, center_y)
        self.radius = radius

    def __str__(self):
        return '(' + str(self.center) + ',' + str(self.radius) + ')'

    def calculate_area(self):
        return math.pi * self.radius ** 2


# p4 = Point(3,4)
# print(p4.distance_from_origin())
# s1 = Square(1,2,3,4)
# print(s1.bottom_left)
# print(s1.top_right)
# print(s1)
#
# c1 = Circle(1,2,5)
# print(c1)
#
# s2 = Square(0,0,4,4)
# print(s2)
# print(s2.calculate_area())
# print(c1.calculate_area())


def in_square(p, sq):
    p_in_s = False
    if sq.bottom_left.x <= p.x <= sq.top_right.x and sq.bottom_left.y <= p.y <= sq.top_right.y:
        p_in_s = True
    else:
        p_in_s = False

    return p_in_s


# point1 = Point(5,1)
# square1 = Square(0,0,4,4)
# print(in_square(point1, square1))


def in_circle(p, circ):
    is_inside = False
    if ((p.x - circ.center.x)**2 + (p.y - circ.center.y)**2) > circ.radius**2:
        is_inside = False
    else:
        is_inside = True
    return is_inside


# p = Point(0.5,0.5)
# circ1 = Circle(0,0,1)
# print(in_circle(p, circ1))

master_circle = Circle(0,0,10)
master_square = Square(-5,-5,5,5)

randoms = []
count = 0
while count < 10000:
    x_rand = range(-5,5,0.001)
    y_rand = range(-5,5,0.001)
    randoms.append(Point(x_rand, y_rand))
    count += 1

in_circ = 0
in_sq = 0
for i in randoms:
    result = in_circle(i, master_circle)
    if result:
        in_circ += 1
    result2 = in_square(i, master_square)
    if result2:
        in_sq += 1

print(in_circ, in_sq)
print(in_circ/in_sq)