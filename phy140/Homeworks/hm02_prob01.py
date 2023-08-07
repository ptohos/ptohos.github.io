#!/usr/bin/python3


# Get the year from the user.
year = int(input("Please enter a year.\n"))

# Assume we have a leap year, by default.
result = 1

# If it's not divisible by 4, it's not a leap year.
if year%4 != 0:
    result = 0
    
# Also, screen for 1700, 1800, 1900, etc. which are also not leap years.
elif year%100 == 0 and year%400 != 0:
    result = 0
    
# Print the end result.
if result == 1:
    print(year,"was a leap year.")
else:
    print(year,"was not a leap year.")
    
print("done")
quit()
