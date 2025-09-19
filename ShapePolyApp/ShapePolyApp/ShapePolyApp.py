import math


class Shape:

    def __init__(self, name="Non-Descript Shape"):
        self.name = name

    def Area(self):
        return None;

    def Perimeter(self):
        return None;
    
    def Describe(self):
        return "Non-Descript Shape"

    def __str__(self):
        self.Describe()


class Circle(Shape):

    def __init__(self, radius=1.0, name="Circle"):
        self._radius = radius
        self.name = name;
        super().__init__(name)

    @property
    def radius(self):
        return self._radius;

    @radius.setter
    def radius(self, value):
        self._radius = value

    def Area(self):
        return math.pi * self._radius * self._radius

    def Perimeter(self):
        return 2 * math.pi * self._radius

    def Describe(self):
        return f"A {self.name} with a radius of {self._radius} circumference of {self.Perimeter}."



class Rectangle(Shape):
    def __init__(self, width=1.0, height=1.0, name="Rectangle"):
        self._width = float(width)
        self._height = float(height)
        super().__init__(name)
        
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


    @property
    def width(self):
        return self._width;

    @width.setter
    def width(self, value):
        self._width = value


    def Area(self):
        return self._width * self._height

    def Perimeter(self):
        return 2 * (self._width + self._height)

    def Describe(self):
        return f"A {self.name} with a width of {self._width} and a height of {self._height}."


class Square(Rectangle):
    def __init__(self, side=1.0, name="Square"):
        super().__init__(side, side, name)

    def Area(self):
        return super().Area()

    def Perimeter(self):
        return super().Perimeter()

    def Describe(self):
        return super().Describe()

circle1 = Circle(2.0, "Circle_1")
circle2 = Circle(9.0, "Circle_2")
rect1 = Rectangle(10, 20, "Rectangle_1")
rect2 = Rectangle(20, 30, "Rectangle_2")
square1 = Square(10, "Square")

shapes = [circle1, circle2, rect1, rect2, square1]

print("--- Polymorphism check ---")
for s in shapes:
    # Match example’s style (Name Area = value). Keep 5-dec precision.
    print(f"{s.name} Area = {round(s.Area(), 5)}")

print()
print("--- Getter/setter check ---")

# Circle: change radius
print(f"{circle1.name} Current: {int(circle1.radius)} {round(circle1.Area(), 5)}")
circle1.radius = circle1.radius * 2
print(f"{circle1.name} Doubled: {int(circle1.radius)} {round(circle1.Area(), 5)}")

# Rectangle: change width and height (your class uses width/height, not length/width)
print(f"{rect1.name} Current: {int(rect1.width)} {int(rect1.height)} {round(rect1.Area(), 5)}")
rect1.width = rect1.width * 2
rect1.height = rect1.height * 2
print(f"{rect1.name} Doubled: {int(rect1.width)} {int(rect1.height)} {round(rect1.Area(), 5)}")

# Square: you inherit Rectangle, so edit width/height (there is no square1.side in your code)
print(f"{square1.name} Current: {int(square1.width)} {round(square1.Area(), 5)}")
square1.width = square1.width * 2
square1.height = square1.height * 2
print(f"{square1.name} Doubled: {int(square1.width)} {round(square1.Area(), 5)}")


