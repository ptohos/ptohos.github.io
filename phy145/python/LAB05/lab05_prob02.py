#!/usr/bin/python3

def greet(msg='Good Afternoon,',*args):
    for i in args:
        print(msg + i)
    return

greet('Hello ', 'Fotis', 'Maria', 'Nick', 'George')


#==============
# Na simeiwthei oti an meta to *args xreiazontan na exoume
# kapoio allo orisma, tote auto tha eprepe na itan orisma
# me keyword gia na apofeuxthei sygxisi
#==============

def greeting(msg='Good Morning,', *args, cnt):   # Dilwsi keyword 
    j = cnt
    for i in args:
        j+=1
        print(msg + i + ' ' + str(j))

greeting('Hello ','Fotis','Maria','Nick','George',cnt=0)  # Xrisi tou keyword
                                                          # gia arxiki timi 0
