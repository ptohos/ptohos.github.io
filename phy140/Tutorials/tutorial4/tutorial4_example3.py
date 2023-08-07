#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to nested loops

Links:
https://www.w3schools.com/python/python_for_loops.asp

'''
print("\n=== Nested for-loop example:")    
for i in range(0, 3, 1):
    print("i = %d" % (i) )
    for j in range(0, 3, 1):
        #print("\ti = %d, j = %d" % (i, j) )
        print("\tj = %d" % (j) )


print("\n=== Another nested for-loop example:")
colour = ["red", "yellow", "green"]
fruit  = ["strawberry", "banana", "apple"]
for c in colour:
    for f in fruit:
        # The "inner loop" will be executed one time for each iteration of the "outer loop"
        print(c, f)
    #print("\n")


print("\n=== A double-nested for-loop example:")
# Outer loop from 2 to 3
for i in range(3, 0, -1):

    # Inner loop
    for c in "ABC": #"ROYGBIV":

        # Second inner loop
        for d in ["x", "y", "z"]: #["SATURDAY" , "SUNDAY"]:
            print("\t", i, c, d)
        print("")
print("=== Finished nested for-loops")


print("\n=== A nested while-loop:")
i = 10
j = 0
while i > 0:
    while j < 4:
        print("\t\ti = %d, j = %d" % (i, j) )
        j+=1
    print("\ti = %d, j = %d" % (i, j) )
    i -= 1


print("\n=== A nested for-loop and while-loop example:")
num    = None
grades = []
names  = ["Costantinos", "Eleni", "Giorgos", "Myrto"]
for name in names:
    while num not in [i for i in range(0, 10, 1)]:
        try:
            num = int(input("Please type a grade for '" + name + "' in range [0, 9]: "))            
        except:
            msg = "Invalid input '%s' of type %s (not type integer). Please try again" % (num, type(num))
            print(msg)
    grades.append(num)
    num = None
    
if len(grades) != len(names):
    print("List length mismatch! (%d != %d)" % (len(grades), len(names)))
else:
    print("\n=== Printing the grades of %d students: ", len(grades) )
    for i in range(0, len(grades), 1):
        print("\t", names[i], grades[i])
                   
print("\n=== Quit!")
quit()
