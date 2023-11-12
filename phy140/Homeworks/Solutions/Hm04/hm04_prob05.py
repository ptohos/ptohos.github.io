from sympy.abc import x
from sympy import sin, series
from sympy.utilities.lambdify import lambdify

import numpy as np
import matplotlib.pyplot as plt


func = sin(x)/x
taylor = series(func, n=6).removeO()

evalfunc = lambdify(x, func, modules=['numpy'])
evaltaylor = lambdify(x, taylor, modules=['numpy'])

t = np.linspace(-5.5, 5.5, 100)
plt.plot(t, evalfunc(t), 'b', label='sin(x)/x')
plt.plot(t, evaltaylor(t), 'r', label='Taylor')
plt.legend(loc='best')
plt.xlim(-5.5,5.5)
plt.ylim(-0.5,2.5)
plt.xlabel('x (rad)')
plt.ylabel('sin(x)/x')
plt.show()
