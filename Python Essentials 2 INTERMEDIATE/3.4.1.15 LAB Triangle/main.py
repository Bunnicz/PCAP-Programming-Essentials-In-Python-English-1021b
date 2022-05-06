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


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3

    def perimeter(self):
        abs_x12 = abs(self.vertice1.getx() - self.vertice2.getx())
        abs_y12 = abs(self.vertice1.gety() - self.vertice2.gety())
        len12 = math.hypot(abs_x12, abs_y12)
        abs_x23 = abs(self.vertice2.getx() - self.vertice3.getx())
        abs_y23 = abs(self.vertice2.gety() - self.vertice3.gety())
        len23 = math.hypot(abs_x23, abs_y23)
        abs_x31 = abs(self.vertice1.getx() - self.vertice3.getx())
        abs_y31 = abs(self.vertice1.gety() - self.vertice3.gety())
        len31 = math.hypot(abs_x31, abs_y31)
        return len12 + len23 + len31


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
