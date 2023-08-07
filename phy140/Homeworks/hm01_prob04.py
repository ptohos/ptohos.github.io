#!/usr/bin/python3

MoneyAsked = int(input("Please insert the desired amount (multiple of 5) "))

# Elegxos oti to poso einai pol/sio tou 5 
if MoneyAsked%5 != 0:
    print("The asked amount is not a multiple of 5!")
    print("Please insert another amount")
    MoneyAsked = int(input("Please insert the desired amount (multiple of 5) "))
if MoneyAsked > 1000:
    print("The requested amount exceeds your daily limit of 1000")
    print("Please insert another amount")
    MoneyAsked = int(input("Please insert the desired amount (multiple of 5) "))

#
N50EuNotes = MoneyAsked//100  # Piliko diairesis me 100 mas leei an to poso
                              # einai pollaplasio tou 100
N50EuNotes = N50EuNotes*2     # Arithmos twn xartonomismatwn twn 50 euro
#
Not50Euro = MoneyAsked - N50EuNotes*50 # Poso pou moirazetai se 20,10,5
N20EuNotes = Not50Euro // 20           # Arithmos xartonomismatwn twn 20 Euro
Not20Euro = Not50Euro - N20EuNotes*20  # Poso pou menei moirazetai se 10,5
N10EuNotes = Not20Euro // 10           # Arithmos xartonomismatwn twn 10 Euro
Not10Euro = Not20Euro - N10EuNotes*10  # Poso pou menei moiraetai se 5 euro
N5EuNotes = Not10Euro//5               # Arithmos xartonomismatwn twn 5 Euro
if (N5EuNotes > 1) :                   # Prepei na einai to polu 1 xartonomisma 
    print("The remaining amount should be multiple of 5Euro bill")
    print("But I see %d xartonomismata" % N5EuNotes)
    print("Something is wrong")

else:
    print("The amount of Euros requested is %d" % MoneyAsked)
    print("You will receive it in the following denominations:")
    print("%2d BankNotes of 50Euro" % N50EuNotes)
    print("%2d BankNotes of 20Euro" % N20EuNotes)
    print("%2d BankNotes of 10Euro" % N10EuNotes)
    print("%2d BankNotes of  5Euro" % N5EuNotes)
