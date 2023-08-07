#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
figsize = (12, 5)

def Deriv(theta, w):
    dw = -np.sin(theta)*g/L - b/(L*m)*w  # gwniaki epitaxunsi
    dtheta = w                           # gwniaki taxutita
    return dtheta, dw

def EulerStep(theta, w, dt):
    dtheta, dw = Deriv(theta, w)
    w = w + dw*dt
    theta = theta + dtheta*dt
    return theta, w

def EulerSolution(theta0, w0, dt, n):
    theta = (n + 1)*[0]    # Arxikopoiisi tou pinaka tis thesis
    w = (n + 1)*[0]        # Arxikopoiisi tou pinaka tis gwniakis taxutitas
    
    theta[0] = theta0      # Arxikes sunthikes
    w[0] = w0              # gia thesi kai taxutita
    for i in range(n):
        theta[i + 1], w[i + 1] = EulerStep(theta[i], w[i], dt) 

    return theta, w

g = 9.81    # m/s^2. Epitaxunsi tis barititas 
m = 1.      # kg. maza
L = 1.      # m. Mikos ekkremous
w0 = 10     # 1/s. Arxiki gwniaki taxutita
theta0 = 3. # rad. Arxiki gwnia
T = 20.     # Sunolikos xronos prosomoiwsis. 
nTimeSteps = 100000  # Arithmos xronikwn vimatwn
b = 0.5     # kg m. Suntelestis antistasis

time = np.linspace(0, T, nTimeSteps + 1)
theta, angvelo = EulerSolution(theta0, w0, T/float(nTimeSteps), nTimeSteps)

plt.figure(figsize=figsize)
plt.title("Angular position")
plt.plot(time, theta, "m")
plt.xlabel(r"$time$, [s]")
plt.ylabel(r"$\theta(t)$, [rad]")
plt.show()

#==================
# Animation
#==================
x = np.sin(theta)                                # Mikos ekkremous 1 kai theta
y = -np.cos(theta)                               # i gwniaki thesi simfwna me ta
                                                 # parapanw tis methodou Euler
from matplotlib import animation
FPS=30                                           # Arithmos frames/sec

# Set up the figure
fig = plt.figure(figsize=(6, 6))
ax = plt.axes(xlim=(-1.1, 1.1), ylim=(-1.1, 1.1))
ax.set_aspect('equal')
ax.grid(True)
#ax.axis('off')

# Orismos twn stoixeiwn tou animation
rod, = ax.plot([],[], color="grey", linewidth=2) # To nima tou ekkremous
ball = plt.Circle((x[0], y[0]), 0.1, fc="grey")  # H maza anaparistatai me kuklo
ax.add_patch(ball)                               # Gemisma tou kuklou

rod, = plt.plot([],[],linewidth=2)
ball.center = plt.plot(x[0],y[0])

# Arithmos twn frames 
framesNum = int(FPS*time[-1])

def init():
    rod.set_data([],[])
    ball.center=(x[0],y[0])
    return rod, ball

# H sunartisi pou kaleitai gia to animation. Kaleitai diadoxika
def animate(j):
    i = j*int(nTimeSteps/framesNum)
    ball.center = (x[i], y[i])                  # H thesi tou KM tou ekkremous
    rod.set_data([0, x[i]], [0, y[i]])          # H grammi tou nimatos
    return rod, ball
# Create animation
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=framesNum, interval=1000/FPS, blit=True, repeat=True)

# save the animation
anim.save('damped_pendulum.mp4',fps=30)

plt.show()
