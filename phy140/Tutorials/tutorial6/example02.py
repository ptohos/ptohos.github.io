#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to open a file, writing, and closing. File modes:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

Links:
https://www.w3schools.com/python/python_file_handling.asp
https://www.askpython.com/python/built-in-methods/open-files-in-python
'''

# Variable definition
filePath = "example02.txt" #full path needed
fileMode = "w"
print("=== Open file '%s' in '%s' mode. " % (filePath, fileMode) )
f = open(filePath, fileMode)
f.write("Hello world!")
f.close()


# Lets read the file
fileMode = "r"
print("=== Open file '%s' in '%s' mode. " % (filePath, fileMode), end="") # reminder
f = open(filePath, fileMode)
print("The contents are: ", end="\n")
contents = f.read()
print(contents)
print(type(contents)) # string!

# Some revision of try
try:
    f.write("This will fail to write because the file is in '%s' mode!" % (fileMode) )
except:
    print("=== Closing file '%s'" % (filePath) )
    f.close()


print("\n=== Quit!")
quit()
