name_str = "Fotios Ptochos"
first = name_str[:6]
last =  name_str[7:]
print("First Name:",first, "Last Name:", last)

# alternative 1
first = name_str[:name_str.find(' ')]
last  = name_str[name_str.find(' ')+1:]

print("First Name:",first, "Last Name:", last)

# alternative 2
first = name_str.split()[0]
last  = name_str.split()[1]

print("First Name:",first, "Last Name:", last)

