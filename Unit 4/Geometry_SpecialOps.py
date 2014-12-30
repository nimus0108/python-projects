import math

class Point (object):
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return("(" + str(self.x) + "," + str(self.y) + ")")

class Shape (object):
    count = 0

    def __init__ (self, shape_type):
        self.shape_type = shape_type
        Shape.count += 1

    def __str__ (self):
        return self.shape_type + "; Area = %.2f; Perimeter = %.2f" % (self.get_area() , self.get_perimeter())

    def get_area (self):
        return -1

    def get_perimeter (self):
        return -1

    def dilate (self, factor):
        pass

class Circle (Shape):
    def __init__ (self, center, radius=1):
        super(Circle, self).__init__("Circle")
        self.center = center
        self.radius = radius

    def get_area (self):
        return math.pi * self.radius ** 2

    def get_perimeter (self):
        return 2 * math.pi * self.radius

    def dilate (self, factor):
        self.radius *= factor

    def __str__(self):
        return "Circle at " + str(self.center) + " with radius " + str(self.radius)

    def __lt__(self, right):
        return self.radius < right.radius

    def __gt__(self, right):
        return self.radius > right.radius

    def __eq__(self, right):
        return self.radius == right.radius

    def __add__(self, right):
        new_radius = (self.radius + right.radius)
        new_x = (self.center.x + right.center.x) / 2
        new_y = (self.center.x + right.center.x) / 2

        p = Point(new_x, new_y)
        c = Circle(p, new_radius)
        return "Circle at (" + str(new_x) + "," + str(new_y) + ") with radius " + str(new_radius)
class Square (Circle):
    def __init__ (self, center, radius=1):
        super (Square, self).__init__(center)
        self.shape_type = "Square"

    def get_area (self):
        return (2*self.radius) ** 2

    def get_perimeter (self):
        return (2 * self.radius) * 4


class Rectangle (Shape):
    def __init__ (self, pt1, pt2):
        super(Rectangle, self).__init__("Rectangle")
        self.pt1 = pt1
        self.pt2 = pt2

    def get_length (self):
        return abs(self.pt2.x - self.pt1.x)

    def get_width (self):
        return abs(self.pt2.y - self.pt1.y)

    def get_area (self):
        return self.get_length() * self.get_width()

    def get_perimeter (self):
        return 2 * (self.get_length() + self.get_width())

    def dilate (self, factor):
        self.pt1.x *= factor
        self.pt2.x *= factor
        self.pt1.y *= factor
        self.pt2.y *= factor

def main() :
    p1 = Point(2,5)
    p2 = Point(3,7)
    c1 = Circle(p1, 10)
    c2 = Circle(p2, 5)

    print("c1: " + str(c1))
    print("c2: " + str(c2))

    c3 = c1 + c2
    print("c3 : " + str(c3))


main()