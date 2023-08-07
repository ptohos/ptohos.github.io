#!/usr/bin/python3
'''
 This program will convert temperatures (Celsius/Fahrenheit)
'''
print('This program converts temperatures (Celsius/ Fahrenheit)')
print('Give (C) to convert Celsius to Fahrenheit')
print('Give (F) to convert Fahrenheit to Celsius')

#Enter choice  Fahrenheit or Celsius
choice = input('Give F or C: ')

# Input temperature
temp=float(input('Give the temperature to convert: '))

if choice == 'C':
   # Calculate in Fahrenheit
   Fahrenheit=32+temp*(9/5)
   print(str(temp)+' degrees Celsius are '+ str(Fahrenheit) + ' degrees Fahrenheit.')
elif choice == 'F':
   # Calculate in Celsius
   Celsius = (temp-32)*(5/9)
   print(str(temp)+' degrees Fahrenheit are ' + str(Celsius) + ' degrees Celsius.')
else:
   print("You gave wrong choice")
