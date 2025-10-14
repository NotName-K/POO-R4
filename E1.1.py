class Shape:
    def __init__(self):
        pass

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        area = self.length * self.width
        return area

    def compute_perimeter(self):
        perimeter = 2 * (self.length) + 2 * (self.width)
        return perimeter
class square(Shape):
    def __init__(self, side):
        self.side = side

    def compute_area(self):
        area = self.side ** 2
        return area
    def compute_perimeter(self):
        perimeter = 4 * self.side
        return perimeter

if __name__ == "__main__":
    rect1 = Rectangle(100, 50)
    square1 = square(100)
    print(rect1.compute_area())
    print(rect1.compute_perimeter())
    print(square1.compute_area())
    print(square1.compute_perimeter())