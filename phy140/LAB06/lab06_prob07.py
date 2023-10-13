
#!/usr/bin/python3

from math import sqrt

inpfile=input('Give the name of the file ')
file2read = open(inpfile,'r')
A = []

for lines in file2read:
    try:
        numb = int(lines.strip())
    except:
        continue
    A += [numb]

file2read.close()
sumsq = 0.0
proda = 1.0
asum  = 0.0
for inum in range(len(A)):
    sumsq += A[inum]*A[inum]
    proda *= (1-A[inum])
    asum  += A[inum]

average = asum/len(A)
sumdv = 0.0
for inum in range(len(A)):
    sumdv += (A[inum] - average)*(A[inum]-average)
sigma = sqrt(sumdv/len(A))

#================
# H tupiki apoklisi mporei na grafei ws eksis:
# Sum(A_N^2 + <x>^2 -2*A_N*<x>) = Sum(A_N^2) + Sum(<x>^2) - 2*<x>Sum(A_N)
# = Sum(A_N^2) + N<x>^2 - 2*<x>*(N*<x>) = Sum(A_N^2) - N*<x>^2
#================
sigma = sqrt((sumsq - len(A)*average*average)/len(A))

outfile=open("lab06_prob07_results.dat","w")
outfile.write(50*'=')
outfile.write('Statistical information')
outfile.write('(a) To athroisma twn tetragwnwn einai:%.1f'%sumsq)
outfile.write('(b) To ginomeno twn orwn [1-A1]*[1-A2]:%6.3E'%proda)
outfile.write('(c) H mesi timi twn orwn einai:%.4f'%average)
outfile.write('(d) H tupiki apoklisi einai:%.4f'%sigma)
outfile.write(50*'=')
outfile.close()
