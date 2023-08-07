#!/usr/bin/python3

#==================================================
# H ennoia tis akribeias pou anaferei i askisi
# simainei oti i diafora tou olikou athroismatos
# tis seiras otan prosthetoume ton k-oro tha
# prepei na einai mikroteri apo tin akribeia.
# Diladi i apoliti timi tou orou pou prostithetai
# einai mikroteri apo tin epithymiti akribeia
#
# Se arketes periptwseis kai gia tin apofugi
# afairesis poli megalwn orwn einai kalo na
# brisketai mia sxesi pou sundeei tous orous
# tis seiras metaksu tous. Diladi na brisketai
# mia sxesi pou na sundeei ton proigoumeno
# me ton epomeno oro. Etsi apofeugontai
# megaloi ypologismoi pou emperiexoun dunameis,
# pol/smous, paragontika klp kathws episis
# apofeugetai o upologismos kathe fora olokliris
# tis seiras
#
# Tha ypologisoume tin apeiri seira:
#  y = f(x) = 0.6 - 1/x + 1/(3x^3) - 1/(5x^5)...
# sto diastima timwn tou x [xmin,xmax] me vima xstep
#==================================================
import numpy as np

epsi=float(input("Give the required precision "))
xmin,xmax=input("Give the range of the xvalues [xmin,xmax] ").split()
xmin = float(xmin)
xmax = float(xmax)
xstep=float(input("Give the step size for scanning the interval "))

filename='Seira.txt'            # The filename
outfile=open(filename,'w')      # Open the file to write
outfile.write(' {0:8s}  {1:5s} {2:5s}\n'.format('xvalues','Sum','Terms Used'))
for x in np.arange(xmin,xmax+xstep,xstep):
    nterms_used = 0
    sumall = 0.6         # The 1st term
    nterm  = 1
    try: 
        term   = -1/x
    except:
        print("x takes 0 value - Division by zero")
        print("the sum can not be calculated")
        outfile.close()
        exit()
    while np.abs(term) > epsi:
        nterms_used += 1
        sumall = sumall + term
        nold   = nterm                     # Kratame ton proigoumeno suntelesti
        nterm  = nterm + 2                 # O suntelestis tou neou orou.
        term   = -term * nold/(x*x)/nterm  # O neos oros prokuptei apo ton
                                           # proigoumeno diairontas me x^2 kai
                                           # pol/zontas me ton proigoumeno
                                           # syntelesti (1,3,5,7) kai diairontas
                                           # me ton neo syntelesti (3,5,7,...)
                                           # Parallila allazoume prosimo
                                           # O parapanw tropos apofeugei ton
                                           # upologismo megalwn arithmwn kathe
                                           # fora. i.e. 1      1         1
                                           #           ---  = --- * 3 * ---
                                           #           5x^5   3x^3      5*x^2

    outfile.write('{:5.1f} {:10.5f} {:8d}\n'.format(x,sumall,nterms_used)) 
outfile.close()
