#!/usr/bin/python3

string1 = "How"
string2 = "are you my friend"
int1 = 34
int2 = 942885
float1 = -3.0
float2 = 3.14158265358793E-14
print(string1)
print(string1 + " " + string2)
# Oi diadoxikes {} tha typwsoyn tis times sto format 
print( "A. {} {} ".format(string1, string2) )
# H timi sta aristera toy : deixnei poio stoixeio tis listaas tou formata tha
# typwthei. O xaraktiras sta deksia tou : deixnei ti morfopoisi pou tha
# akoloythithei: s-string, d-integer,f-float, e-exponential. Ta noumera pou
# emfanizntai 6.3f h 8.3f simainei kratise toulaxiston 6 i 8 theseis  gia ton
# arithno me toulaxiston 3 psifia meta tin ypodiastoli. 
print( "B. {0:s} {1:s}".format(string1,string2) )
print( "C. {0:s} {0:s} {1:s} - {0:s} {1:s}".format(string1,string2) )
print( "D. {0:10s}{1:5s}".format(string1, string2) )
print( " **** ")
print(int1, int2)
print( "E. {0:d} {1:d}".format(int1, int2) )
print( "F. {0:8d} {1:10}".format(int1 int2) )
print( "G. {0:0.3f}".format(float1) )
print( "H. {0:6.3f}".format(float1) )
print( "I. {0:8.3f}".format(float1) )
print( 2*"J.  (0:8.3f)    ".format(float1) )
print( " *****")
print( "K. {0:0.3e}".format(float2) )
print( "L. {0:12.3e}".format(float2) )
# O arithmos gia ektupwsei einai 3.142E-14 epomenws zitwntas 3 dekadika sto M
# den prokeitai na emfanistei tipota giati o arithmos ksekina apo to 14 psifio
# ara tha apokopei
print( "M. {0.12.3f}".float(float2) )
print( " *****")
print("N. 12345678901234567890"
print("O. {0:s} -- {1:8d}, {2:10.3e}".format(string2, int1, float2) 
