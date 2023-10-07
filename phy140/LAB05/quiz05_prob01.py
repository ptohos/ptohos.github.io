def append_middle(s1,s2):
   print("Original strings are:",s1,s2)
   # sto mesi tis s1
   if (len(s1)%2 == 1):
       m1=int(len(s1)/2)+1
   else:
       m1=int(len(s1)/2)
   x =s1[:m1:] #οι χαρακτήρες μέχρι το μέσο
   x = x+s2    #ένωση της s2 με το 1ο μισό της s1
   s3 = x+s1[m1:] #ένωση με το 2ο μισό της s1
   print("After the concatenation:",s3)
append_middle(input("s1: "),input("s2: "))
