# POO-R4
![Logo](https://github.com/NotName-K/POO-R2/blob/main/Screenshot%202025-09-23%20110719.png?raw=true)
### Ejercicios sobre polimorfismo....
## Ejercicio 1
### SuperClase Shape() y rectangulo
```python
class Shape:   ## Superclase
    def __init__(self):   
        pass

    def compute_area(self):    # Calculo de Area
        pass

    def compute_perimeter(self):     # Calculo de perimetro
        pass 

class Rectangle(Shape):    # Clase Rectangulo
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def compute_area(self):    # Area del Rectangulo
        area = self.length * self.width
        return area

    def compute_perimeter(self):   # Perimetro del Rectangulo
        perimeter = 2 * (self.length) + 2 * (self.width)
        return perimeter

class square(Shape):    # Clase Caudrado 
    def __init__(self, side):
        super(),__init__()
        self.side = side
        
    def compute_area(self):  # Area del cuadrado
        area = self.side ** 2
        return area
    def compute_perimeter(self):    # Perimetro del cuadrado
        perimeter = 4 * self.side
        return perimeter
    
if __name__ == "__main__":
    rect1 = Rectangle(100, 100)
    square1 = square(100)
    print(rect1.compute_area())
    print(rect1.compute_perimeter())
    print(square1.compute_area())
    print(square1.compute_perimeter())
```
## Ejercicio 2
### Superclase Shape() con varias caracteristicas
##### Clases Point y Line
```python
class Point:
    def __init__(self, x: float, y:float):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value

    def compute_distance(self, point: "Point") -> float:
        return ((self.__x - point.get_x()) ** 2 + (self.__y - point.get_y()) ** 2) ** (1/2)


class Line:
    def __init__(self, p_s: Point, p_e: Point):
        self.__p_s = p_s
        self.__p_e = p_e
        self.__length = self.__p_s.compute_distance(self.__p_e)

    def get_start_point(self):
        return self.__p_s

    def set_start_point(self, p_s: Point):
        self.__p_s = p_s
        self.__update_length()

    def get_end_point(self):
        return self.__p_e

    def set_end_point(self, p_e: Point):
        self.__p_e = p_e
        self.__update_length()

    def get_length(self):
        return self.__length

    def __update_length(self):
        self.__length = self.__p_s.compute_distance(self.__p_e)
```
#### Clase Shape
```python
class Shape:
    def __init__(self, vertices=None, edges=None, inner_angles=None, is_regular=False):
        self.__vertices = vertices or []
        self.__edges = edges or []
        self.__inner_angles = inner_angles or []
        self.__is_regular = is_regular

    def get_vertices(self):
        return self.__vertices

    def set_vertices(self, vertices):
        self.__vertices = vertices

    def get_edges(self):
        return self.__edges

    def set_edges(self, edges):
        self.__edges = edges

    def get_inner_angles(self):
        return self.__inner_angles

    def set_inner_angles(self, angles):
        self.__inner_angles = angles

    def get_is_regular(self):
        return self.__is_regular

    def set_is_regular(self, value):
        self.__is_regular = value

    def compute_area(self):
        raise NotImplementedError("Método implementado por la subclase")

    def compute_perimeter(self):
        raise NotImplementedError("Método implementado por la subclase")

    def compute_inner_angles(self):
        raise NotImplementedError("Método implementado por la subclase")
```
#### Clase Rectangle y Square
```python
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width

        vertices = [Point(0, 0),
            Point(length, 0),
            Point(length, width),
            Point(0, width)]

        super().__init__(vertices, is_regular=False)

    def get_length(self):
        return self.__length

    def set_length(self, value):
        self.__length = value

    def get_width(self):
        return self.__width

    def set_width(self, value):
        self.__width = value

    def compute_area(self):
        return self.__length * self.__width

    def compute_perimeter(self):
        return 2 * (self.__length + self.__width)

    def compute_inner_angles(self):
        return [90, 90, 90, 90]

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)
        self.set_is_regular(True)

    def compute_perimeter(self):
        side = self.get_length()
        return 4 * side

    def compute_area(self):
        side = self.get_length()
        return side ** 2
```
#### Clase Triangle y herencias
```python
class Triangle(Shape):
    def __init__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Los lados no forman un triángulo válido.")
        self.__a = a
        self.__b = b
        self.__c = c
        super().__init__(is_regular=False)

    def get_sides(self):
        return self.__a, self.__b, self.__c

    def compute_perimeter(self):
        return self.__a + self.__b + self.__c

    def compute_area(self):
        s = self.compute_perimeter() / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def compute_inner_angles(self):
        a, b, c = self.get_sides()
        A = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
        B = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
        C = 180 - A - B
        return [A, B, C]


class Isosceles(Triangle):
    def __init__(self, equal_side, base):
        super().__init__(equal_side, equal_side, base)

    def compute_area(self):
        base = self.get_sides()[2]
        equal = self.get_sides()[0]
        height = math.sqrt(equal**2 - (base**2) / 4)
        return (base * height) / 2


class Equilateral(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
        self.set_is_regular(True)

    def compute_area(self):
        a = self.get_sides()[0]
        return (math.sqrt(3) / 4) * (a ** 2)


class Scalene(Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

class RightTriangle(Triangle):
    def __init__(self, base, height):
        hypotenuse = math.sqrt(base**2 + height**2)
        super().__init__(base, height, hypotenuse)

    def compute_area(self):
        return (self.get_sides()[0] * self.get_sides()[1]) / 2
```
## Reto 4
