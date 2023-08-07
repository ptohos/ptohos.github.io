import numpy as np

class Circle():
    def __init__(self, r):
        self.radius = r
    def __str__(self):
        return f'The circle has a radius of {self.radius}'
    def area(self):
        return self.radius*self.radius*np.pi
    def perimeter(self):
        return 2*self.radius*np.pi

    def test(rad):
        A = Circle(rad)
        print(A)
        print(f'The perimeter of the circle is {A.perimeter()}')
        print(f'The area of the circle is {A.area()}')
