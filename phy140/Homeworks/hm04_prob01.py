#!/usr/bin/python3

from math import sqrt

def triangle(corners):
    '''
    Sunartisi pou epistrefei to emvado kai perimetro enos trigwnou
    oi korufes tou opoiou orizontai apo to orisma corners pou einai
    einai mia lista 3 stoixeiwn to kathena apo ta opoia einai lista
    kai periexei tis suntetagmenes x kai y tis antistoixis koryfis.
    
    To emvado upologizetai apo to ekswteriko ginomeno 2 opoiodipote
    pleurwn tou trigwnou. To ekswteriko ginomeno duo dianusmatwn
    isoutai me to embado toy parallilogrammou pou orizoun ta 2
    dianysmata kai epomenws tha isoutai me to diplasio tou embadou
    twn 2 trigwnwn pou orizei mia opoiadipote diagwnios tou
    paralliligrammou.
    
    Estw i pleura a pou orizetai apo tis korufes 1 (x1,y1) kai 2(x2,y2)
    kai i pleyra b pou orizetai apo tis korufes 1 (x1,y1) kai 3 (x3,y3)
    Estw i kai j ta monadiaia dianusmata stous aksones x kai y. 
    Tote a=(x2-x1)i + (y2-y1)j  
         b=(x3-x1)i + (y3-y1)j
    A = 0.5*|a x b| = 0.5*|(x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)| 
    Input argument:
       corners: list of 3 lists 
    Output:
       A : embado
       C : perimetro
    '''
    x1 = corners[0][0]; y1 = corners[0][1]
    x2 = corners[1][0]; y2 = corners[1][1]
    x3 = corners[2][0]; y3 = corners[2][1]
    A = 0.5*abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)
    C = sqrt((x2-x1)**2 + (y2-y1)**2) + \
        sqrt((x3-x2)**2 + (y3-y2)**2) + \
        sqrt((x1-x3)**2 + (y1-y3)**2)
    return A, C

def input_coordinates():
    corners1 = []
    st=['x','y']
    for j in range(2):
        cv = input("Give the %s-coordinate of the vertex "%st[j])
        corners1.append(float(cv))
    return corners1


print(40*("="))
print("Check the area of triangle with vertices = [(-3, 0), (3, 0), (0, 4)]")
corners=[]
for j in range(3):
    print("Give the coordinates of vertex %d"%(j+1))
    corners.append(input_coordinates())
A1, C1 = triangle(corners)
print('Area of triangle:%.2f\nPerimetros of triangle:%.2f\n'%(A1,C1))
print(40*("="))

print("Area of the polygon with vertices = (0, 0), (2, 4), (3, 0.5), (4,3)")
corners=[] ; Area=[]; Perim=[]
for k in range(2):               # Polygon apoteleitai apo 2 triangles
    print("Give the vertices of the %d triangle"%k)
    corners=[]
    for j in range(3):
        print("Give the coordinates of vertex %d"%(j+1))
        corners.append(input_coordinates())
    A1, C1 = triangle(corners)      # Area and perimeter of triangle
    Area  +=[A1]                     # Keep the info on a list
    Perim +=[C1]
print('Area of polygon:%.2f'%(Area[0]+Area[1]))
print(40*("="))
