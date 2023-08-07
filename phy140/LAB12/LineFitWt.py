import numpy as np
import matplotlib.pyplot as plt

def LineFitWt(x,y,dy):
    """
    Fit to straight line of the form  y = bx + a
    Inputs: x,y. and the error of y (dy)
    Output: slope and y - intercept of best fit to data
    """
    dy2 = dy**2
    norm = (1./dy2).sum()
    xhat = (x/dy2).sum() / norm
    yhat = (y/dy2).sum() / norm
    slope = ((x-xhat)*y/dy2).sum()/((x-xhat)*x/dy2).sum()
    yint = yhat - slope*xhat
    dy2_slope = 1./((x-xhat)*x/dy2).sum()
    dy2_yint = dy2_slope * (x*x/dy2).sum()/norm
    return slope, yint, np.sqrt(dy2_slope), np.sqrt(dy2_yint)

def Reduced_Chisquare(x, y, dy, slope, yint):
    chisq = (((y - yint - slope*x)/dy)**2).sum()
    return chisq/float(x.size-2)


#.... Read data from a file
t, N, dN = np.loadtxt("FitData.dat", skiprows=2, unpack=True)


#.... Make the data linear
X=t
Y=np.log(N)
dY=dN/N

#.... Fit the transformed datat X, Y , DY -> parameters A(intercept) & B(slope)
#.... and calculate the uncertainties

B, A, dB, dA = LineFitWt(X, Y, dY)

#... Return the chi square
Rchisq = Reduced_Chisquare(X, Y, dY, B, A)

#... Determination of the fitting parameters for exponential function 
#... N = N0 exp(-t/tau)
N0 = np.exp(A)
tau = -1.0/B

#... the uncertainty
dN0= N0* dA
dtau = tau**2 * dB

#... Plotting
#... The fit function (line) needs two points 
Xext = 0.05 * (X.max() - X.min())
Xfit = np.array([X.min()-Xext, X.max()+Xext])
Yfit = A + B * Xfit

#... The plot
fig, ax = plt.subplots()  # H sunartisi subplots dimiourgei fig. and subplot
                          # kai epistrefei fig:figure and ax:axes.Axes 
ax.errorbar(X,Y,dY, fmt="oC0")
ax.plot(Xfit, Yfit, "-C1", zorder=-1)
ax.set_xlim(0,100)
ax.set_ylim(1.5, 7)
ax.set_title(r"$\mathrm{Fit\ to:}\ \ln N = -t/\tau + \ln N_0$")
ax.set_xlabel("$t$")
ax.set_ylabel("ln($N$)")
ax.text(50,6.6,"A = ln N0 = {0:0.2f} $\pm$ {1:0.2f}".format(A,dA))
ax.text(50,6.3,"B = -1/tau = {0:0.4f} $\pm$ {1:0.4f}".format(-B,dB))
ax.text(50,6.0,"$\chi_r^2$ = {0:0.3f}".format(Rchisq))
ax.text(50,5.7,"N0 = {0:0.0f} $\pm$ {1:0.1f} days".format(N0,dN0))
ax.text(50,5.4,"tau = {0:0.1f} $\pm$ {1:0.1f} days".format(tau,dtau))
fig.savefig("FitData.pdf")
plt.show()
