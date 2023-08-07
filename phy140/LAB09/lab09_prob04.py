from math import tanh
def bisection(f, x_L, x_R, eps, return_x_list=False):
    f_L = f(x_L)
    if f_L*f(x_R) > 0:
        print("Error! Function does not have opposite \
                 signs at interval endpoints!")
        sys.exit(1)
    x_M = float(x_L + x_R)/2.0
    f_M = f(x_M)
    iteration_counter = 1
    if return_x_list:
        x_list = []

    while abs(f_M) > eps:
        if f_L*f_M > 0:   # i.e. same sign
            x_L = x_M
            f_L = f_M
        else:
            x_R = x_M
        x_M = float(x_L + x_R)/2
        f_M = f(x_M)
        iteration_counter += 1
        if return_x_list:
            x_list.append(x_M)
    if return_x_list:
        return x_list, iteration_counter
    else:
        return x_M, iteration_counter

def f(x):
    return tanh(x)
    #return x**2 - 9

a = float(input("Give the lower limit for bracketing the solution: "))
b = float(input("Give the upper limit for bracketing the solution: "))
eps = float(input("Give the desired accuracy :"))
interm_sol = input("Do you want intermediate solutions? [Y/N]")

do_interm_sol = False
if interm_sol.upper() == 'Y':
    do_interm_sol = True

solution, no_iterations = bisection(f, a, b, eps, do_interm_sol)

print("Number of function calls: %d" % (2 + no_iterations))
if do_interm_sol:
    for i in range(len(solution)):
        print("Intermediate solution %2d: %10.9f"%(i+1,solution[i]))
else:
    print("Solution is: %10.9f"%(solution))
