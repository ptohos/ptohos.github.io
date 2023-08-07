import matplotlib.pyplot as plt
import numpy as np

nb=int(input("Give the desired number of points "))
x = np.linspace(0,4*np.pi, nb)    # dimiourgia enos np pinaka megethous 33
y = np.sin(x)
plt.plot(x,y)
plt.show()


