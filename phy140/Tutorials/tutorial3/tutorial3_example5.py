#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3 <filename>

Usage (v2):
python3 
import <filename>

Description:
More on logical/comparison operators and their combination.

Links:
https://www.pythontutorial.net/python-basics/python-logical-operators/
''' 
yes = True
no  = False

# If can be used by itself (without else)
if (yes):
    msg = "=== Hello world!"
    print(msg)
    
if (no):
    msg = "=== This will never be printed"
    print(msg)
    
if (yes or no):
    msg = "=== This will always be true"
    print(msg)

if (not (yes or no)):
    msg = "=== This will also never be printed"
    print(msg)


print("\n=== Direct use of logical operators booleans")
value = 9.99
print("\tIs the value less than 10?", (value < 10) )
print("\tIs the value not greater than 10?", (not value > 10) )
print("\tIs the value in the range (5, 10]?", (value > 5 and value < 10) )

print("\n=== Direct Precedence of not/and/or operators (descending order):\n\t1) not\n\t2) and\n\t3) or")


a = True
b = True
c = False
d = True
msg = "\n=== Examples for precedence of Logical Operators"
msg += " (a = %s, b = %s, c = %s, d = %s)" % (a, b, c, d)
print(msg)

print("\ta or b and c = ", (a or (b and c) ) )
print("\ta and b or c and d = ", ( (a and b) or (c and d) ) )
print("\ta and b and c or d = ", ( ((a and b) and c) or d) )
print("\tnot a and b or c = ", ( ((not a) and b) or c) )


msg = "\n=== Take-away message: Use brackets to make sure!"
print(msg)

quit()

