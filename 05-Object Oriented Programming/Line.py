import math


class Line(object):

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def distance(self):
        return math.sqrt((self.point2[0] - self.point1[0])**2 + (self.point2[1] - self.point1[1])**2)

    def slope(self):
        return (self.point2[1] - self.point1[1])/(self.point2[0] - self.point1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

