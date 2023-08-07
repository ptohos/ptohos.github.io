#!/usr/bin/python3

'''
  Mia class gia upologismous me algebra diastimatwn
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
class IntervalMath(object):
    """
    Paradeigmata:
    >>> from IntervalMath import IntervalMath as I
    >>> v0 = I(4, 6)
    >>> t = I(0.6, 0.7)
    >>> g = 9.81
    >>> y = v0*t - 0.5*t**2
    >>> print 'v0 =', v0, ', t =', t, ', y =', y
    v0 = [4, 6] , t = [0.6, 0.7] , y = [2.155, 4.02]
    >>> print float(y)  # mean value of y interval
    3.0875
    >>> # computing with mean values:
    >>> v0 = float(v0);  t = float(t);  y = v0*t - 0.5*t**2
    >>> print y
    3.03875
    >>> R = I(6*0.9, 6*1.1)   # 20 % error
    >>> V = (4./3)*pi*R**3
    >>> V
    IntervalMath(659.584, 1204.26)
    >>> print V
    [659.584, 1204.26]
    >>> print float(V)
    931.922044761
    >>> R = float(R)
    >>> V = (4./3)*pi*R**3
    >>> print V
    904.778684234
    """

    def __init__(self, lower, upper):
        '''Dimiourgia diastimatos me basi to xamilotero kai upsilotero orio.'''
        if lower <= upper:
            self.lo = float(lower)
            self.up = float(upper)
        else:
            print('lower limit %s must be smaller than upper limit %s' %
                   (lower, upper))
            exit()

    @staticmethod       # H @staticmethod dimiourgei mia methodo (n2interval(n))
    def n2interval(n):  # pou den energei sta obj tis class i tin class alla
                        # mono sta dedomena. Ayto xreiazetai gia tin periptwsi
                        # pou exoume na kanoume prakseis metaksu enos object
                        # tis klasis kai enos arithmou gia paradeigma pou den
                        # mporei na ginei an o arithmos brisketai sta aristera
                        # tis praksis kai to antikeimeno tis class deksia
                        # Ayto exei sinepeies stis prakseis episis. Gia oles tis
                        # prakseis tha prepei na oristoun __r<praksi>__() opou
                        # an den mporei na ginei i praksi me __<praksi>__ logw
                        # tou tupou tou antikeimenoun sta aristera, proxwra me
                        # tin methodo __r<praksi>__() me to antikeimeno sta
                        # deksia 
        """Metatropi tou n pou einai arithmos i diastima, se diastima."""
        if type(n) is int or type(n) is float : # Einai arithmos kai epistrefei
            return IntervalMath(n, n)           # diastima [n,n]
        elif type(n) is IntervalMath : # Einai diastima kai epistrefei diastima
            return n
        else:
            print('operand %s %s must be number of '\
                  'interval' % (n, type(n)))
            exit()
            
    def _limits(self, other):
        other = IntervalMath.n2interval(other)       # Efarmogi tis static
        return self.lo, self.up, other.lo, other.up  # methodou

    def __add__(self, other):
        a, b, c, d = self._limits(other)
        return IntervalMath(a + c, b + d)

    def __sub__(self, other):
        a, b, c, d = self._limits(other)
        return IntervalMath(a - d, b - c)

    def __mul__(self, other):
        a, b, c, d = self._limits(other)
        return IntervalMath(min(a*c, a*d, b*c, b*d),
                            max(a*c, a*d, b*c, b*d))

    def __truediv__(self, other):
        a, b, c, d = self._limits(other)
        # [c,d] den mporei na periexei 0:
        if c*d <= 0:
            print('Interval %s cannot be denominator because '\
                  'it contains zero')
            exit()
        return IntervalMath(min(a/c, a/d, b/c, b/d),
                            max(a/c, a/d, b/c, b/d))

    def __radd__(self, other):
        other = IntervalMath.n2interval(other)
        return other + self

    def __rsub__(self, other):
        other = IntervalMath.n2interval(other)
        return other - self

    def __rmul__(self, other):
        other = IntervalMath.n2interval(other)
        return other*self

    def __rdiv__(self, other):
        other = IntervalMath.n2interval(other)
        return other/self

    def __pow__(self, exponent):
        if type(exponent) is int:
            p = 1
            if exponent > 0:
                for i in range(exponent):
                    p = p*self
            elif exponent < 0:
                for i in range(-exponent):
                    p = p*self
                p = 1/p
            else:
                p = IntervalMath(1, 1)
            return p
        else:
            print('exponent must int')
            exit()

    def __eq__(self, other):
        return self.lo == other.lo and self.up == other.up

    def __neq__(self, other):
        return not self.__eq__(other)

    def __float__(self):
        return 0.5*(self.lo + self.up)

    def width_in_percent(self):
        """
        Epistrofi tou eurous tou diastimatos ws tois ekato tis mesis timis
        >>> a = IntervalMath(10*0.9, 10*1.1)  # 10% ekaterwthen tou 10
        >>> a.width_in_percent()
        20.0
        """
        m = float(self)
        w2 = m - self.lo
        p2 = w2/m*100
        return 2*p2

    def tolist(self):
        return [self.lo, self.up]

    def __str__(self):
        return '[%g, %g]' % (self.lo, self.up)

    def __repr__(self):
        return '%s(%g, %g)' % \
               (self.__class__.__name__, self.lo, self.up)


def main():
#    from hm04_prob03 import IntervalMath as I

    I = IntervalMath
    Tm = 0.45
    t = I(0.95*Tm, 1.05*Tm)
    y0 = I(0.99,1.01)
    g = 2*y0/t**2
    print('\n')
    print('t =', t, ', y =', y0, ', g =', g)
    print('g width:{:5.2f}%'.format(g.width_in_percent()))
    print('mean g  =', float(g))
    print('mean y0 =', float(y0))
    print('mean t  =', float(t))
    print('g mean  =', 2*float(y0)/float(t)**2) 
    print('\n')
    from math import pi
    Rm=6
    R = I(Rm*0.9, Rm*1.1)   # 20 % error
    V = (4./3)*pi*R**3
    print('R =', R, 'V =', V)
    print('R width:{0:5.2f}%'.format(R.width_in_percent()))
    print('V width:{0:5.2f}%'.format(V.width_in_percent()))
    print('R mean:', float(R))
    print('V mean:', float(V))
    print('V calc:', (4./3)*pi*(float(R))**3)
main()

    
