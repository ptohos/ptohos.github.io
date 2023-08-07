import numpy as np

class Polynomial(object):
    def __init__(self, coefficients):
        self.coeff = coefficients
        
    def __call__(self, x):
        """Evaluate the polynomial."""
        s=0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s
    
    def __add__(self, other):
        '''Epistrefei self + other as Polynomial object.
        Duo periptwseis:
        (1)
        self:     X X X X X X X
        other:    X X X
        (2)
        self:     X X X 
        other:    X X X X X X X
        '''
        # Ksekinoume me to poluwnumo me ti megalyteri lista kai prosthetoume
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]            # copy!
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:]           # copy!
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)

    def __sub__(self, other):
        '''Epistrefei self - other as Polynomial object.'''
        m = len(self.coeff)
        n = len(other.coeff)
        diff = m - n
        if  m == n:
            result_coeff = self.coeff[:]
            for i in range(n):
                result_coeff[i] -=other.coeff[i]
        elif m > n:
            result_coeff = self.coeff[:]
            for i in range(n):
                result_coeff[i] -= other.coeff[i]
        else:
            result_coeff = other.coeff[:]
            for i in range(n):
                result_coeff[i] = -result_coeff[i]
                if i < m: result_coeff[i] += self.coeff[i]            
        return Polynomial(result_coeff)

    def __mul__(self, other):
        u = self.coeff
        v = other.coeff
        m = len(u) - 1
        n = len(v) - 1
        result_coeff = [0 for i in range(m+n+1)]
        for i in range(0, m+1):
            for j in range(0, n+1):
                result_coeff[i+j] += u[i]*v[j]
        return Polynomial(result_coeff)

    def __truediv__(self,other):
        '''Epistrefei to pililo q kai ypoloipo r tis diairesis poluwnumwn
           Orismata:  self einai to diairetaio poluwnumo 
                      other einai o diairetis poluwnumo.'''
        u = self.coeff[::-1]      # se antitheti fora
        v = other.coeff[::-1]     # 
        m = len(u)
        n = len(v)
        if n < 0:
            print("Diairetis polynomial einai 0")
            print("den mporei na ginei diairesi")
            exit()
        scale = 1/v[0]
        for i in range(m-n+1):
            u[i] *= scale
            coeff = u[i]
            for j in range(1,n):
                u[i+j] += -v[j]*coeff
        sep = -n+1
        q=u[:sep]
        r=u[sep:]
        q=q[::-1]
        r=r[::-1]
        return Polynomial(q), Polynomial(r)
            
    def differentiate(self):
        """Paragwgisi tou polynomial kai antikatastasi tou."""
        for i in range(1, len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
        del self.coeff[-1]

    def derivative(self):
        """Antigrafi toy poluonumou kai epistrofi tis paragwgou tou."""
        dpdx = Polynomial(self.coeff[:])  # make a copy
        dpdx.differentiate()
        return dpdx
    
    def __str__(self):
        s = ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
        # Fix layout
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^1 ', 'x ')
        if s[0:3] == ' + ':  # remove initial +
            s = s[3:]
        if s[0:3] == ' - ':  # fix spaces for initial -
            s = '-' + s[3:]
        pos=s.find('*')
        if s[pos:pos+2]=='*1':
            s = s[:pos]+s[pos+2:]
        return s

def main():
    x = [1,-1]                # Oi stathero suntelestes
    y = [0,1,0,0,-6,-1]
    a = Polynomial(x)
    b = Polynomial(y)
    print('a = ',a)
    print('b = ',b)
    add = a + b               # prosthaisi
    print('a+b = ',add)
    dif = b - a               # diafora
    print('a-b = ',dif)
    mul = a * b               # pol/smos
    print('a*b = ',mul)
    p,r = b/a                 # diairesi - epistrefei piliko kai upoloipo
    print('b/a: Piliko =',p)  
    print('b/a: Ypoloipo ',r) 
    w=p*a
    w=w+r                     # epalitheusi
    print('Epalitheusi diairesis: a*p+r =',w)
    deriv = b.derivative()    # Ypologismos tis paragwgou
    print('Derivative tou b = ',deriv)
    xx=a(4)                   # Timi tou poluwnimou a gia x=4  
    print('Timi tou a gia xx=%d:%d'%(4,xx))
        
main()
