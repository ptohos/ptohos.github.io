import matplotlib.pyplot as plt
import numpy as np

#(a) Prwto ypoerwtima
k = 9.9E9
R = 5E-2
z = 2*R
Q = 5
w = z/R
E = k*Q/R**2 * w/(w**2+1)**(3/2)
print("H entasi tou pediou se apostasi z=2R einai E = ",E,"N/C")
#
#
#(b) Orizoume to x pou einai mia list me times apo -3, 3 me vima 0.1
x=np.linspace(-3,3.,61)
y=abs(x/(x**2+1)**(3/2))
plt.figure(figsize=(6,4))
plt.plot(x,y,'b-')
plt.xlabel(r'z/$R$')
plt.ylabel(r'E(kQ/$R^2$)')
plt.text(-2.9,0.35,r'E = $\frac{kQ}{R^2}\frac{z}{(z^2+1^2)^{3/2}}$')
plt.rc('font',size=10)
plt.xlim(-3,3.)
plt.ylim(0.,0.4)
plt.grid(True)
plt.show()
