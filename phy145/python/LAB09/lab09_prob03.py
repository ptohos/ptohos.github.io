#!/usr/bin/python3

#======================
# Xrisi twn methodwn Trapeziou, Endiamesou Simeiou kai Simpson
# gia oloklirwsi sunartisewn
#======================
# Xrisi mesw klasis
#======================
import numpy as np
import math

class Integrator(object):
    def __init__(self,lowerlim,upperlim,npoints):
        self.lowerlim=lowerlim
        self.upperlim=upperlim
        self.npoints=npoints
        self.points, self.weights = self.construct_method()

    def construct_method(self): # Ginetai overwrite apo tin paragwgi class
                                # An ksexasoume na tin orisoume stin paragwgi
                                # class, tote i yparksi aytis edw tha mas to
                                # dwsei to print msg 
        
        print("Method %s is not implemented yet"%self.__class__.__name__)

    def integrate(self,f):
        sum = 0
        for i in range(len(self.weights)):
            sum += self.weights[i]*f(self.points[i])# weights einai suntelestes
        return sum                                 # twn diaforwn methodwn pou
                                                   # pol/zoun tin sunartisi 
class Midpoint(Integrator):   # subclasses
    def construct_method(self):
        lowerlim = self.lowerlim
        upperlim = self.upperlim
        npoints = self.npoints
        h = (upperlim - lowerlim)/npoints
        x = np.linspace(lowerlim+0.5*h,upperlim-0.5*h, npoints)
        w = np.zeros(len(x)) + h
        return x,w

class Trapezoidal(Integrator):
    def construct_method(self):
        x = np.linspace(self.lowerlim,self.upperlim, self.npoints)
        h = (self.upperlim - self.lowerlim)/(self.npoints-1)
        w = np.zeros(len(x)) + h
        w[0] /= 2                  # Sti methodo tou trapeziou, to prwto kai 
        w[-1] /= 2                 # teleutaio simeio einai misa
        return x, w

class Simpson(Integrator):
    def construct_method(self):
        if self.npoints %2 != 1:  # Prepei na exoume peritta simeia
                                  # gia artio plithos diastimatwn
            #print("n=%d prepei na einai peritto, prosthetoume 1"%self.npoints)
            self.npoints += 1
        x = np.linspace(self.lowerlim, self.upperlim, self.npoints)
        h = (self.upperlim - self.lowerlim)/(self.npoints - 1)*2
        w = np.zeros(len(x))
        w[0:self.npoints:2] = h * 1.0/3.0
        w[1:self.npoints-1:2] = h * 2.0/3
        w[0] /=2
        w[-1] /=2
        return x, w

def main():
    def f1(x):
        return np.sin(x)
    def f2(x):
        return 5*x*x + 3*x - 2
    def f3(x):
        return 1/(1+x**2)

    lowerlimits=[0, 0, 0]
    upperlimits=[np.pi, 3, 1]
    npoints = [50, 1000, 5000]
    functs  = [f1, f2, f3]
    functna = ['f1','f2','f3']
    methods = [Midpoint, Trapezoidal, Simpson]
    print("No. Steps   Function   Midpoint    Trapezoidal    Simpson")
    for npoint in npoints:
        i = -1
        print(' %5d'%npoint,end=' ')
        for func in functs:
            i +=1
            if i==0: print(' %9s'%functna[i],end=' ')
            if i>0:  print(' %16s'%functna[i],end=' ')
            for method in methods:
                integrator = method(lowerlimits[i],upperlimits[i],npoint)
                Integral = integrator.integrate(func)
                print(' %11.6f '%Integral,end=' ')
            print()

main()
