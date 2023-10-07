#!/usr/bin/python3
"""
Computes the area of a polygon from vertex 
coordinates only.
"""
def polyarea(x, y):
    n = len(x)
    # Arxikopoiisi tou embadou me tis koryfes pou den summetexoun
    # sto loop ws pros tis korufes. Diladi i prwti me tin teleutaia
    area = x[n-1]*y[0] - y[n-1]*x[0]  
    for i in range(0,n-1,1):
        area += x[i]*y[i+1] - y[i]*x[i+1]
    return 0.5*abs(area)


# Test the 5-gone
x = [0,2,2,1,0]
y = [0,0,2,3,2]
print("The area of the pentagon (true value = 5): ", polyarea(x,y))
# Test orthogonio
x = [0,2,2,0]
y = [0,0,2,2]
print("The area of the orthogoniou (true value = 4): ", polyarea(x,y))
# Test triangle
x = [0,2,0]
y = [0,0,2]
print("The area of the orthogoniou (true value = 2): ", polyarea(x,y))

