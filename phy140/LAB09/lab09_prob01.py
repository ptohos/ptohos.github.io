def Newton(f, dfdx, x, eps, return_x_list=False):
    f_value = f(x)
    iteration_counter = 0
    if return_x_list :
        x_list = []
        
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - float(f_value)/dfdx(x)
        except:
            print("Error! - derivative zero for x = ", x)
            sys.exit(1)     # Abort with error

        f_value = f(x)
        iteration_counter += 1
        if return_x_list:
            x_list.append(x)
            
    # Sto simeio ayto fthanoume otan exei brethei lusi i
    # exoume kseperasei ton arithmo twn prospatheiwn
    if abs(f_value) > eps:
        iteration_counter = -1
    if return_x_list:
        return x_list, iteration_counter
    else:
        return x, iteration_counter

def f(x):
    return x**2 - 9

def dfdx(x):
    return 2*x

return_x_list = False
xstart = float(input("Give an initial guess for the solution "))
eps = float(input("Give the desired accuracy "))
int_sols = input("Do you want intermediate solutions? [y/n] ")
if int_sols.upper() == 'Y' :
    return_x_list = True
    
solution, no_iterations = Newton(f, dfdx, xstart, eps, return_x_list)

if return_x_list :
    sol = solution[-1]
    for i in range(len(solution)):
        print("Solution number %2d: %16.15e"%(i,solution[i]))
else:
    sol = solution
if no_iterations > 0:    # Solution found
    print("Number of function calls: %d" % (1 + 2*no_iterations))
    print("A solution is: %16.15e" % (sol))
else:
    print("Solution not found!")
