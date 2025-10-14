# POO-R4
![Logo](https://github.com/NotName-K/POO-R2/blob/main/Screenshot%202025-09-23%20110719.png?raw=true)
### Ejercicios sobre polimorfismo....
## Ejercicio 1
### 1. SuperClase Shape() y rectangulo
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
## Reto 4
