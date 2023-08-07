#================
# from MyVector import MyVector, MyPolarVector
# a = MyVector(1,2,3)
# b = MyVector(2,3,4)
# print(a)
# c = a.dot(b)
# print(c)
# d = a.cross(b)
# print(d)
# f = a*4
# print(f)
# g = a/4
# print(g)
# h=a.unit()
# a.norm()
#===============

import math

class MyVector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return 'MyVector (%f,%f,%f)' % (self.x,self.y,self.z)

    def __add__(self,other):
        return MyVector(self.x+other.x, self.y+other.y,self.z+other.z)

    def __sub__(self,other):
        '''subtracts vector'''
        return MyVector(self.x-other.x,self.y-other.y,self.z-other.z)
    
    def __mul__(self,scalar):
        '''multiplies vector by scalar'''
        return MyVector(scalar*self.x,scalar*self.y,scalar*self.z)
    
    def __truediv__(self,scalar):
        '''divides vector by scalar'''
        return MyVector(self.x/scalar,self.y/scalar,self.z/scalar)
     
    def norm(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def unit(self):
        '''creates a unit vector'''
        return self/self.norm()

    def dot(self,other):
        '''computes dot product'''
        return self.x*other.x+self.y*other.y+self.z*other.z

    def cross(self,other):
        '''computes cross product'''
        new_x = self.y*other.z-self.z*other.y
        new_y = self.z*other.x-self.x*other.z
        new_z = self.x*other.y-self.y*other.x
        return MyVector(new_x,new_y,new_z)

class MyPolarVector(MyVector):
    '''vector in polar coordinates'''
    def __init__(self,r,theta,phi):
        '''constructor'''
        MyVector.__init__(self,
                          r*math.cos(theta)*math.cos(phi),
                          r*math.cos(theta)*math.sin(phi),
                          r*math.sin(theta))

    def r(self):
        return self.norm()
    
    def phi(self):
        return math.atan2(self.y,self.x)
    
    def theta(self):
        return math.asin(self.z/self.norm())
