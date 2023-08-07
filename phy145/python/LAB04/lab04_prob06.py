#!/usr/bin/python3

filename = input("Enter file:") 
inpfile = open(filename)
counts = dict() 
for line in inpfile:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
bigcount = None
bigword  = None
# Eyresi tis leksis me megaluteri suxnotita emfanisis
for word,count in counts.items():             # H suxnotita count einai 
    if bigcount is None or count > bigcount:  # megaluteri apo tin megaluteri 
        bigword = word                        # yparxousa i einai tin prwti 
        bigcount = count                      # fora pou to bigcount einai
print(bigword, bigcount)                      # akoma none. 
#============================
# Mporoume na taksinomisoume
# to dictionary me basi
# tis times tis kathe leksis
#============================
a = list(sorted(counts.items(), key=lambda cnt: (cnt[1], cnt[0]), reverse=True))
for i in range(min(10,len(a))):
    print("%5s  %4d"%a[i])

