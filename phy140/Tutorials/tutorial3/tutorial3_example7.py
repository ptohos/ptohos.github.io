#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3 <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to lists and their manipulation

Links:
''' 

myList = []
print("1) myList = %s, len(myList) = %s" % (myList, len(myList)))

myList.append('abc')
print("2) myList = %s, len(myList) = %s" % (myList, len(myList)))

myList.append(100)
print("3) myList = %s, len(myList) = %s" % (myList, len(myList)))

myList.append("")
print("4) myList = %s, len(myList) = %s" % (myList, len(myList)))

myList.extend( ["P", "I", "N", "K", "", "F", "L", "O", "Y", "D"] )
print("5) myList = %s, len(myList) = %s" % (myList, len(myList)))

nBlank = myList.count("")
print("6) myList = %s, len(myList) = %s, nP = %s" % (myList, len(myList), nBlank))

iBlank = myList.index("") # returns the smallest index that an object of type "" was found
print("7) myList = %s, len(myList) = %s, nP = %s, iBlank = %s" % (myList, len(myList), nBlank, iBlank))

print("8a) myList = %s" % (myList) )
myList.insert(0, "A") # returns the smallest index that an object of type "" was found
print("8b) myList = %s" % (myList) )

myList.reverse()
print("9) myList = %s" % (myList) )

myList.reverse()
print("10) myList = %s" % (myList) )

A = myList.pop(0)
print("11) myList = %s, A = %s" % (myList, A) )


print("\n")
myList1 = [i for i in range(0, 10)]
myList1.reverse()
print("1) myList1 = %s" % (myList1) )

myList1.sort()
print("2) myList1 = %s" % (myList1) )
quit()
