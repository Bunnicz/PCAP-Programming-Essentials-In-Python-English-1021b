import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self._Point__x

    def gety(self):
        return self._Point__y

    def distance_from_xy(self, x, y):
        abs_x = abs(self.getx() - x)
        abs_y = abs(self.gety() - y)
        return math.hypot(abs_x, abs_y)

    def distance_from_point(self, point):
        abs_x = abs(self.getx() - point.getx())
        abs_y = abs(self.gety() - point.gety())
        return math.hypot(abs_x, abs_y)


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
