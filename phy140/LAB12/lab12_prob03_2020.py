#!/usr/bin/python3
'''
  To problima einai provlima euresis tis rizas mias eksiswsis kai 
  mporeite na xrisimopoiisete mia apo tis duo methodous pou kserete. 
  H dyskolia tis askisis einai na vroume tin eksiswsi pou tha prepei 
  na lusoume. Apo to provlima kseroume oti i efaptomeni tis elleipsis 
  sto simeio pou psaxnoume (xo,yo) perna kai apo to simeio A me 
  suntetagmenes (xA,yB). Epomenws i eksiswsi tis eutheias tis efaptomenis
  grafetai ws: 
                klisi = (yo-yA)/(xo-xA)                    (1)
  H klisi omws tis efaptomenis einai isi me tin paragwgo tis eksiswsis 
  tis elleipsis sto simeio (xo,yo). H eksiswsi tis elleipsis einai 
  x^2/a + y^2/b = 1 opote kai i paragwgos tis einai 
                y' = -(b/a)(x/y)
  kai sto (xo,yo) tha einai:          y'=-(b/a)(xo/yo)     (2)
  Apo (1) kai (2) exoume:
                -(b/a)(xo/yo) = (yo-yA)/(xo-xA)            (3)
  To simeio ayto ikanopoiei kai tin eksiswsi tis elleipsis
                 yo^2/b = 1 - xo^2/a => bxo^2+ayo^2 = ab   (4)
  Kanontans tis prakseis stin (3) kai antikathistontas tin (4) 
  tha paroume:
                 ayAyo + bxoxA = ab                        (5)
  Epomenws exoume to systima:
       (ayA)yo + (bxo)xA = ab => (bxA)xo = ab - (ayA)yo    (6a)
         bxo^2 + ayo^2 = ab => bxo^2 = ab - ayo^2          (6b)
  Ypswnoume tin (6a) sto tetragwno
        (bxA)^2xo^2  = (ab)^2+(ayA)^2yo^2 - 2(a^2byA)yo =>
        (bxA^2)bxo^2 = (ab)^2+(ayA)^2yo^2 - 2(a^2byA)yo    (7) 
  Lunoume tin (6b) ws pros bxo^2 kai antikathistoume stin (7)
   (bxA^2)(ab-ayo^2) = (ab)^2+(ayA)^2yo^2 - 2(a^2byA)yo =>
   ab^2xA^2 - (abxA^2)yo^2 = (ab)^2+(ayA)^2yo^2 - 2(a^2byA)yo =>
   Meta apo algebrikes prakseis kataligoume:
       yo^2(bxA^2+ayA^2) - (2abyA)yo + b^2(a-xA^2) = 0     (8)
 
  Alla xA = -8, yA = -1 enw a=25 kai b=16. Antikatastasi dinei:
       1049yo^2 + 800yo - 9984                             (9)
  Theloume epomenws na vroume tis rizes tis eksiswsis aytis
  me ti methodo tou Newton i me ti methodo tis dixotomisis
  Analytika oi rizes tis eksiswsis aytis einai:
    yo(1) = +2.727227
    yo(2) = -3.489858
  Kai profanws theloume ti thetiki riza opws zita i askisi.
  Kserontas to yo mporoume na broume to xo apo tin (5)
    xo = (ab - ayAyo)/(bxA) = (400 + 25*2.727227)/(-8*16) = -3.6576615 
  Enw i klisi tis efaptomenis sto simeio ayto tha einai:
    y' = -(16/25)(-3.6576615/2.727227) = 0.85834563
  Epomenws i eksiswsi tis eytheias tha einai:
    y = 0.85834563*(x+8) - 1
================================================================
'''
import numpy as np
import matplotlib.pyplot as plt

def abline(x,slope,xp,yp):
    intercept = (yp-xp*slope)
    yvals = slope*x + intercept    
    return yvals

def func1(x):
    return 4*np.exp(-2*x)

def func2(x):
    return 0.5*x**2

def func(x):
    return 1049*x**2 + 800*x - 9984        # H eksiswsi (9)

def d1x(x):
    return 2098*x + 800

'''================================'''
def newton(x0,f,df,eps,istepmx):
    istep = 0
    flag = 0
    condition = True
    #
    while condition:
        if df(x0) == 0:
            flag = 2
            break
#
        error=f(x0)/df(x0)
        x1 = x0 - error    # The new solution 
        x0 = x1            # The new solution becomes the old solution for the
        istep = istep+1
        if np.abs(error) < eps:
            condition = False
#            
        if istep > istepmx:
            flag = 1
            break
#
    return x0,flag,istep

#.... Main program
#.... Input parameters 0, 3, 1E-6

xlo  = float(input('Give the low limit of the interval pou periexei ti lusi '))
xup  = float(input('Give the upper value of the interval pou periexei ti lusi '))
epsi = float(input('Give the desired precision for the solution '))
mxit = 20
#... Newton
xguess = (xlo+xup)/2   # To meso tou diastimatos ws i arxiki lusi
xnewton, flag, niter = newton(xguess,func,d1x,epsi,mxit) 
print('\n ****** Results by Newton''s method *******') 
if flag == 0:
    print('The solution is {:.15e}'.format(xnewton))
    print('{:2d} iteration were needed'.format(niter))
    print('The value of the function is f(x=',xnewton,') = ',func(xnewton))
elif flag == 1:
    print('No solution was reached because no convergence')
    print('{:2d} iteration were used of max {:2d}'.format(niter,mxit))
else:
    print('Derivative is zero at the value {:.2e}'.format(xnewtom))
    print('The value of the function is f(x',newton,') = ',func(xnewton))

'''
 Kanoume to grafima twn duo sunartisewn gia na 
 broume peripou to simeio tomis tous
'''
x = np.arange(-10.1,10.1,0.0001)
y1 = 4*np.sqrt(1-x**2/25)
y2 =-y1

b_el = 16
a_el = 25
y0 = xnewton                       # H lusi einai gia to y tou simeiou epafis
x0 =-np.sqrt(a_el*(1-y0**2/b_el))  # To x vrisketai apo tin eksiswsi tis ellipsis
xA = -8.
yA = -1.
#.... Slope apo tin eksiswsi (3)
slope = -(b_el/a_el)*(x0/y0)
print(slope,x0,y0)
yline = abline(x,slope,xA,yA)
#
plt.plot(x,y1,'b-')
plt.plot(x,y2,'b-')
plt.plot(x,yline,'r--')
plt.plot(xA,yA,'C1s')
plt.plot(x0,y0,'o',markersize=11, fillstyle='none')
plt.text(0,2.5,r'$\frac{x^2}{25}+\frac{y^2}{16} = 1$',fontsize=14)
plt.text(xA*0.95, yA,'A')
plt.text(x0*0.95,y0*0.95,r'$({:.3g},{:.3g})$'.format(x0,y0))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(-8.5,5.5)
plt.ylim(-5,5)
plt.grid(True)
#
plt.show()

