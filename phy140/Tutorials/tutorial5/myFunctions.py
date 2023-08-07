#!/usr/bin/python3
'''
Links:
https://docs.python.org/3/library/functions.html
'''

# Added for example2.py (and example3.py)
def say_hi(name="Alexandros", exampleNum=1, tutorialNum=5, course="PHYS-140"):
    '''
    \param name (str) ..........: Name of user 

    \param tutorialNum (int) ...: The current tutorial number [1,12]

    \param exampleNum (int) ....: The current example number [1,7]]
    
    \param course (str) ........: The title of the course being taken

    \return Nothing
    '''
    print("=== Hello %s! Welcome to example %d of tutorial %d, for course %s!" % (name, exampleNum, tutorialNum, course) )
    
def powerN(x, exp):
    '''
    \param x (int) .....: value for base

    \param exp (int) ...: value for exponent 
    
    \return power(x, exp) = x^{exp}
    '''
    return x**exp

def getTwoInts(msg1="+++ Type value 1: ", msg2="+++ Type value 2: "):
    '''
    \param msg1 (str) ...: The text message printed to the user to inform him of action to be taken for value of x1

    \param msg2 (str) ...: The text message printed to the user to inform him of action to be taken for value of x2

    \return Nothing
    '''
    x1 = int(input(msg1))
    x2 = int(input(msg2))
    return x1, x2

# Added for example4.py
def getList(msg="=== Types values (int) to add to the list. To stop type any input that is non-integer: "):
    '''
    \param msg (str) ...: The text message printed to the user to inform him of action to be taken for value of the numList

    \return list of integers that were given as input by the user
    '''
    print(msg)
    try:
        myList = []
        count  = 0
        while True:
            #myList.append( int(input("\t: ")) )
            myList.append( int(input("\tmyList[%d]: " % (count))) )
            count+=1
    except:
        # if the input is not-integer, just print the list
        print("=== Returning myList: ", myList)
    return myList

def sumList(myList):
    '''
    \param myList (list of int or floats) ...: list of integers to conduct mathematic operation on elements

    \return sum of all list elements (int or float)
    '''
    mySum = 0
    for num in myList:
        try:
            mySum+= num
        except:
            print("=== Error! Cannot add %s to the sum %d" % (num, mySum) )
    return mySum

def prodList(myList):
    '''
    \param myList (list) ...: list of numbers (int or float) to conduct mathematic operation on elements

    \return sum of all list elements (int or float)
    '''
    prod = 1
    for num in myList:
        try:
            prod*= num
        except:
            print("=== Error! Cannot multiply %s to the product %d" % (num, prod) )
    return prod

# def Print(myObjs, mySep=" ", myEnd="\n", myFile=None, myFlush=False):
#     '''
#     Description:
#     Custom print function
# 
#     \param myObjs (object(s))...: the object(s) to be printed
# 
#     \param mySep (str) .........: controls the separator between the printed objects [default: " "]
# 
#     \param myEnd (object(s)) ...: controls the ending of the print message [default: "\n"]
# 
#     \param myFlush (object(s)) .: clearing of the output stream [default: False]
# 
#     \return Nothing
#     '''
# 
#     print(myObjs, sep=mySep, end=myEnd, file=myFile, flush=myFlush)

# Added for example6.py
