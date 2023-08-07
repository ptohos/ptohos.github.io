#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3 <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to try/except

Links:
https://data-flair.training/blogs/python-exception-handling/
''' 

x=1
try:
  print("x = ", x)
except: # NameError:
  print("=== Exception: The variable x is not defined")
finally:
    print("=== This will print no matter what (exception or no exception)")


try:
    newPrice   = float(input("\n=== Type value for new price: "))
    oldPrice   = float(input("=== Type value for old price: "))
    percChange = ((newPrice - oldPrice)*100)/oldPrice
    
    if percChange < 0:
        result = "\tPrice drop of %s %%" % (abs(percChange))
    else:
        result = "\tPrice increase of %s %%" % (abs(percChange))
        
    print(result)

except:
    msg = "Error! Please enter a number (not character) for the prices."
    print(msg)

    
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
# a, b = 1, 0
# try:
#     print("a/b = ", (a/b) )
#     print("This will never be printed. Any statement after an exception in the 'try' block are skipped.")
# except TypeError:
#     print("You added values of incompatible types")
# except ZeroDivisionError:
#     print("You divided by 0")
           
quit()
