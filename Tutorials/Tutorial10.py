class Point:
    def __init__(self, xx=0, yy=0, zz=0):
        self.x = xx
        self.y = yy
        self.z = zz

    def __str__(self):
        return '( ' + str(self.x) + ' ' + str(self.y) + ' ' + str(self.z) + ' )'

    def distance_from_origin(self):
        return round(((self.x**2)+(self.y**2)+(self.z**2))**0.5,3)


p1 = Point()
p2 = Point(1,2,3)
p3 = Point(3,4)
print(p1)
print(p2)
p2dist = p2.distance_from_origin()
print(p2dist)

p1dist = Point.distance_from_origin(p1)
print(p1dist)

p3dist = Point.distance_from_origin(p3)
print(p3dist)

# Q1:D
# Q2:D
# Q3:B

# Tutorial questions

