#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Further information to file handling (open, writing, and closing). Reminder on file modes:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

Links:
https://www.w3schools.com/python/python_file_open.asp
https://www.tutorialspoint.com/python/file_seek.htm
https://www.w3schools.com/python/ref_file_seek.asp
'''

# Variable definition
filePath = "example03.txt" #full path needed
fileMode = "w"
print("=== Open file '%s' in '%s' mode. " % (filePath, fileMode) )
f = open(filePath, fileMode)
for i in range(11):
    f.write("L%d\n" % (i) )
f.close()


# Lets read the file
fileMode = "r"
print("=== Open file '%s' in '%s' mode. " % (filePath, fileMode), end="") # reminder
f = open(filePath, fileMode)
print("The contents are: ", end="\n")
for line in f:
    print(line, end="")

    
# Must go back to line 0 of file before reading again!
f.seek(0)

print("=== Retrieve the file contents as a list with readlines():")
contList = f.readlines()
for row in contList:
    print(row, end="")

print("=== Retrieve the file contents as a list with f.read():")
# Set the position of the read/write pointer within the file to begining (0)
f.seek(0)
print(f.read())
print(type(f.read()))

print("=== Retrieve the file contents as a list with f.read().split():")
f.seek(0) # if not used then get empty list!
print(f.read().split())
print(type(f.read().split()))


print("=== Loop over all lines in the file: ", end="\n")
f.seek(0)
for line in f:
    print(line, end="")


print("=== Alternatively, can loop over the contents list as follows:")
for iRow in range(len(contList)):
    print("contList[%d] = %s" % (iRow, contList[iRow]), end="")

f.seek(0)
f.close()
print("\n=== Quit!")
quit()
