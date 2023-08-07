'''
H askisi ayti exei skopo na anadeiksei pws i methodos Newton douleuei 
alla kai pws mporei na odigithei se mi sygklisi
Ksekinontas me tin timi x0 = 1.08, i methodos Newton sygklinei stin 
riza xsol = 0. To programma paragei mia seira apo grafimata tis 
sunartisis kai tis efaptomenis tis sinartisis se kathe endiamesi lusi.
H efaptomeni pida se diafora simeia prin telika arxisei na sygklinei
stin lusi. 
Stin periptwsi tis x0 = 1.09 i efaptomeni kineitai makria apo ti 
anamenomeni lusi kai sto telos to apotelesma einai nan = not a number 
pou dilwnei oti den exei sugklinei kai upirkse 
diairesi me 0 (h klisi tis efaptomenis einai 0)
'''

from numpy import tanh, linspace
import matplotlib.pyplot as plt

def Newton_check(f, dfdx, x, eps):
    f_value = f(x)
    iteration_counter = 0
    
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            print( 'Current x value: ', x)
            plot_line(f, x, f_value, dfdx(x))
            input('...press enter to continue')
            x = x - float(f_value)/dfdx(x)
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", x)
            sys.exit(1)     # Abort with error

        f_value = f(x)
        iteration_counter += 1

    # Edw erxomaste eite otan exei vrethei lusi
    # i otan exoume ypervei ton arithmo twn prospatheiwn
    if abs(f_value) > eps:
        iteration_counter = -1
    return x, iteration_counter

def f(x):
    return tanh(x)

def dfdx(x):
    return 1 - tanh(x)**2

def plot_line(f, xn, f_xn, slope):
    # Plot both f(x) and the tangent
    x_f = linspace(-2,2,100)
    y_f = f(x_f)
    x_t = linspace(xn-2,xn+2,10)
    y_t = slope*x_t + (f_xn - slope*xn)  # Straight line: ax + b
    plt.figure()
    plt.plot(x_t, y_t, 'r-', x_f, y_f, 'b-')
    plt.grid('on')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

def main():
    solution, no_iterations = \
                      Newton_check(f, dfdx, x=1.09, eps=0.001)

    if no_iterations > 0:    # Solution found
        print("Number of function calls: %d" % (1 + 2*no_iterations))
        print("A solution is: %f" % (solution))
    else:
        print("Solution not found!")

if __name__ == '__main__':
    main()
