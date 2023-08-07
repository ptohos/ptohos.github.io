import numpy as np

class Rectangle():
    def __init__(self, leng, wid):
        self.length = leng
        self.width = wid

    def __str__(self):
        return f'The rectangle has length of {self.length} and width of {self.width}'

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

    def test(in1, in2):
        A = Rectangle(in1,in2)
        print(A)
        print(f'The perimeter of the rectangle is {A.perimeter()}')
        print(f'The area of the rectangle is {A.area()}')
