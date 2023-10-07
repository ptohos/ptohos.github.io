def replace_special(st1,st2):
   print("Original string is:",s1)
   first = True
   for let in st1:
      if let in st2:
        let = "~"
      if first:
        st3 = let
        first = False
      else:
        st3 = st3 + let 
   print("The new string is: ",st3) 

s1 = input("Arxiki str1: ")
s2 = "!@#$%^&*()-_"
replace_special(s1,s2)
