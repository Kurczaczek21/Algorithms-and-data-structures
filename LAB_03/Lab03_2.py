from math_module import Circle, Square,Triangle

circle = Circle(4)
print(circle.area(), circle.circuit())

triangle = Triangle(3, 4, 5)
print(triangle.area(), triangle.circuit())

square = Square(5)
print(square.area(), square.circuit())