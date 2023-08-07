#!/usr/bin/python3

#===========================================================
#  Ypologismos twn polynymvn LEGENDRE. 
#  To programma xrisimopoiei ena 
#  ypoprogramma synartsis gia ton 
#  ypologismo toy Pn(x) toy poluonumou
#  Legendre symfwva me tis anagvgiki sxesi
#             2n-1              n-1
#    Pn(x) = ------ xPn-1(x) - ------Pn-2(x)
#              n                n
#  San efarmogi kai elegxo tou kvdika 
#  to programma ypologizei kai typvnei tis times 
#  tvn polynymvn n=1,2,3,4,5 gia x=0.,0.1,0.2,0.3,...,1.0
#==========================================================
import numpy as np

def PolyLegendre(Npoly,xv):
    #====================================================================
    # Ypologismos poluwnumwn Legendre symfvna me tin anagwgiki sxesi. 
    #
    #  H synartisi einai tis morfis P(N,x), me parametrous
    #  ton akeraio N kai ton pragmatiko X. Oi akraies times
    #  gia NPOL=0 kai NPOL<0 yologizontai kai katopin o deiktis tou
    #  poluwnumou auksanei mexri ti timi NPOL dimiourgontas
    #  ta P1(x), P2(x),...,Pn(x). Kathe stigmi oi times twn 
    #  2 teleutaiwn poluwnumwn kratiountai sti mnimi sa times
    #  twn PVAL0 kai LEGENDRE. Otan o deiktis ginei N i sunartisi dinei 
    #  tin timi tou PLEGENDRE
    #
    #  INPUT parametroi: 
    #        Npoly: taksi tou poluwnumou
    #        xv   : timi tou X
    #====================================================================
    PValue0 = 0.          # Arxiki timi tis sunartisis gia Npoly<0         
    PLegendre = 1.          # Arxiki timi tis sunartisis gia Npoly=0
    #============
    # Exoume tis dyo prwtes times tou poluwnumou
    #============
    for ipol in range(Npoly):
        ipoly = ipol+1
        PLegend  = (2*ipoly - 1)*xv*PLegendre/ipoly   # n-1 oros
        PLegend -= (ipoly - 1) *PValue0/ipoly         # n-2 oros
        PValue0    = PLegendre       # Antikatastasi twn n-1, n-2 orwn
        PLegendre  = PLegend         # me tis nees times
    return PLegendre

#================
#  Main program
#================
nPolmax = int(input("Give the maximum order of the polynomials "))
xmin,xmax=input("Give the range for the xvalues [xmin,xmax] ").split()
xstep = float(input("Give the x-step size "))

xmin = float(xmin)
xmax = float(xmax)

PolMat=[]
istep = 0
for xval in np.arange(xmin,xmax+xstep,xstep):
    istep = istep
    xPol  = []                               # Row gia kathe xval poy exetazoume
    xPol +=[xval]
    for Npol in range(nPolmax):
        Nth_poly = Npol + 1
        pvalue = PolyLegendre(Nth_poly,xval)
        xPol +=[pvalue]
    PolMat +=[xPol]                         # Prosthesi tis grammis me tis times
                                            # twn Npol poluwnumwn gia to xval
print(" %7s    %6s      %6s    %8s    %8s    %8s"%("xvalues","P1(x)", "P2(x)",
                                                   "P3(x)", "P4(x)", "P5(x)"))
for i in range(len(PolMat)):
    for j in range(len(PolMat[0])):
        if j==0:
            print('%6.2f'%PolMat[i][j],end='')
        else:
            print('%12.4f'%PolMat[i][j],end='')
    print()

      
