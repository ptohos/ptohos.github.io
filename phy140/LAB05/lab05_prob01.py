string = str(input("Give a string:"))

print("The first character is:",(string[0]))
print("The last character is:",(string[-1]))
print("The last character is:",(string[len(string)-1]))
print("The first space is in location:",string.find(' '))
print("The first word is:",(string[0:string.find(' ')]))

