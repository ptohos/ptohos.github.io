#=========================-===============
# Se ayta pou akoloythoun dilwnetai i klasi
# ComplexNumber, me mia seira apo methodous
# pou epitrepoun ti dimiourgia migadikwn
# prakseis metaksi antikeimenwn tis klasis
# kathws kai diafores sugkriseis 
# Xrisimopoiountai oi methodoi tis python:
# __add__  gia +
# __sub__  gia -
# __mul__  gia *
# __truediv__ gia /
# __eq__   gia ==
# __ne__   gia !=
# __gt__   gia ">"
# __ge__   gia ">="
# __lt__   gia "<"
# __le__   gia "<="
# __str__  gia printout
# Kai orizontai oi methodoi
# conjugate()
# abs()
# __neg__()
# get_data()
# ======================================
# Paradeigmata xrisis:
#======================
# from lab05_prob05 import ComplexNumber
# a = ComplexNumber(4,3)
# b = ComplexNumber(2,4)
# print(a)
# print(b)
# c = a+b                # Prosthesi  isodunamo me a.__add__(b)
# d = a-b                # afairesi   isodunamo me a.__sub__(b)
# aconj = a.conjugate()  # conjugate tou a  (4-3j)
# amag = abs(a)          # magnitude of a  sqrt(4^2+3^2)
# s = a*b                # multiplication isodunamo me a.__mul__(b)
# z = a/b                # diairesi
# print(s == z)          # tha dwsei False
# print(a!=aconj.conjugate()) # tha dwsei False giati aconj einai o a conjugate
# z.get_data()
#========================================

import math

class ComplexNumber(object):
    def __init__(self, real=0, imag=0):              # i.e. a=ComplexNumber(1,1)
        self.real = real                             # i.e. b=ComplexNumber(2,2)
        self.imag = imag

    def conjugate(self):                             # i.e. c=a.conjugate()
        return ComplexNumber(self.real, -self.imag)
        
    def __add__(self, other):                        # i.e  d=(a+b)
        return ComplexNumber(self.real+other.real,
                             self.imag+other.imag)
    
    def __sub__(self, other):
        return ComplexNumber(self.real-other.real,   # i.e  dd=(a-b)
                             self.imag-other.imag)

    def __mul__(self, other):                        # i.e  ddd=a*b
        return ComplexNumber(self.real*other.real - self.imag*other.imag,
                             self.real*other.imag + self.imag*other.real)
        
    def __truediv__(self, other):                    # i.e. cc=a/b
        conj = other.conjugate()
        den = other * conj
        den = den.real
        num = self*conj 
        return ComplexNumber(num.real/den, num.imag/den)
    
    def __neg__(self):                              # i.e ee=a.__neg__()
        return ComplexNumber(-self.real, -self.imag)

    def __eq__(self, other):                       # i.e print(cc==aa) T or F
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):                       # i.e. print(cc!=aa) T or F
        return not self.__eq__(other) 

    def __str__(self):
        return 'ComplexNumber: (%g+%gj)'%(self.real, self.imag)
    
    def __illegal(self,op):
        return 'Illegal operation "%s" for complex numbers' % op
        
    def __gt__(self, other):
        return self.__illegal('>')

    def __ge__(self, other):
        return self.__illegal('>=')

    def __lt__(self, other):
        return self.__illegal('<')

    def __le__(self, other):
        return self.__illegal('<=')
    
    def __abs__(self):                               # i.e. cc=abs(a)
        return math.sqrt(self.real*self.real + self.imag*self.imag)
    
    def get_data(self):
        print(f'{self.real}+{self.imag}j')


