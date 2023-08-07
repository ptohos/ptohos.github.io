#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to for-loops

Links:
https://www.w3schools.com/python/python_for_loops.asp

'''

print("\n=== Example of for-loop:")
for l in "ALEXANDROS":
    print(l)


print("\n=== Another for-loop example:")    
for x in range(0, 12, 2):
    print("\tx = %d" % (x) )    
print("=== NOTE that the range(0, 12) is not the values of 0 to 12, but the values 0 to 12-step (\ie 0 to 10).")



print("\n=== Another for-loop example:")    
for x in range(10, 0, -1):
    print("\tx = %d" % (x) )
print("=== NOTE that the range(10, 0) is not the values of 10 to 0, but the values 10 to 0-step (\ie 10 to 1).")    


print("\n=== Another for-loop example:")    
for l in ["And then one day you find", "Ten years have got behind you", "No one told you when to run", "You missed the starting gun"]:
    print("\t"+l)
print("=== NOTE that the range(0, 12) is not the values of 0 to 12, but the values 0 to 12-step (\ie 0 to 10).")

print("\n=== Another for-loop example:")    
for i in range(10):
    if i == 0:
        print("\ti = 0")
    elif i == 1:
        print("\ti = %d" % (x) )
    else:
        continue # can stop the current iteration of the loop, and continue with the next


print("\n=== Example with enumerate:")
# iterable	An iterable object
# start	A Number. Defining the start number of the enumerate object. Default 0
echoes = ["The", "echo", "of", "a", "distant", "time", "comes", "willowing", "across", "the", "sand"]
for i, echo in enumerate(echoes, start=0): #enumerate(iterable, start=0)
    print("%i) %s = %s" % (i, echo, echoes[i]))

print("\n=== Quit!")
quit()
