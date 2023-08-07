import numpy as np
import matplotlib.pyplot as plt
from numpy.random import RandomState

n = 100
r = RandomState()

plt.figure(figsize=(8,6))
steps=np.arange(0,100,1)

for j in range(7):
    p = np.zeros(n)
    p[0] = 0.0

    for i in range(n-1):
        if (r.rand() >= 0.5):
            p[i+1] = p[i] + 1
        else:
            p[i+1] = p[i] - 1

    plt.plot(steps,p)
plt.xlabel('Step')
plt.ylabel('Position')
plt.title('1-D Random Walk')
plt.xlim(0,100)
plt.ylim(-20,20)
plt.grid(True)

plt.show()

