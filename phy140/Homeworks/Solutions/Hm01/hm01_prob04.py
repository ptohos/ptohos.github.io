#!/usr/bin/python3

time = float(input("Give the time in the form of [hh.mm] "))
nhours = int(time)                # To akeraio meros mas dinei tis wres
nmin = int(100*(time - nhours))   # O arithmos twn leptwn 
nsec = nhours*3600 + nmin*60

print("Gia xrono",time,"o arithmos twn deyteroleptwn einai",nsec)
