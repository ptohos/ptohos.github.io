from numpy import zeros, linspace, pi, cos, array
import matplotlib.pyplot as plt

omega = 2
P = 2*pi/omega
dt = P/20
T = 3*P
N_t = int(round(T/dt))
t = linspace(0, N_t*dt, N_t+1)

X_rk = zeros(N_t+1)       # Ayto einai to theta
V_rk = zeros(N_t+1)       # Ayto eunai i gwniaki taxutita

# Initial condition
X_0 = 2
X_rk[0] = X_0
V_rk[0] = 0

# Step equations forward in time
for n in range(N_t):
    x_md   = X_rk[n] + V_rk[n]*dt/2           #Miso vima Euler sto meso 
    v_md   = V_rk[n] - omega**2*X_rk[n]*dt/2  #Miso vima Euler sto
    X_rk[n+1] = X_rk[n] + dt*v_md
    V_rk[n+1] = V_rk[n] - dt*omega**2*x_md

fig = plt.figure()
l1, l2 = plt.plot(t, X_rk, 'b-', t, X_0*cos(omega*t), 'r--')
fig.legend((l1, l2), ('RK2', 'exact'), 'upper left')
plt.xlabel('t (s)')
plt.ylabel('Theta (rad)')
plt.show()
plt.savefig('tmp.pdf')

