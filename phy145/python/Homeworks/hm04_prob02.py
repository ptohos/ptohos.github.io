#!/usr/bin/env python3


def hex2dec(hexStr):
    '''
    hex2dec - Metatropi apo 16-diko systima se dekadiko
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''

    dec = 0      # Athroisma apo kathe psifio tou 16dikou systimatos
    # dictionary gia antistoixisi metaksu twn idiaiterwn psifiwn toy 16dikou kai 10dikou
    Hex2DecDict = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
 
    # Ksekinontas apo to pleon simantiko psifio (aristera)
    # metatropi tou 16dikou arithmou se dekadiko
    for hexDigitPos in range(len(hexStr)):  # H thesi tou kathe psifiou 0,1,2...apo aristera
        hexDigit = hexStr[hexDigitPos]      # Eksagwgi tou psifiou stin hexDigiPos
        hexExp = len(hexStr)-hexDigitPos-1  # O ekthetis analoga me ti thesi tou psifiou
        hexExpFactor = 16 ** hexExp         # Ypologismos tis dunamis 
        if '1' <= hexDigit and hexDigit <= '9':
            dec += int(hexDigit) * hexExpFactor
        elif hexDigit == '0':
            pass                            # Den kanoume tipota 
        elif 'a' <= hexDigit.lower() and hexDigit.lower() <= 'f':
            dec += Hex2DecDict[hexDigit] * hexExpFactor  
        else:
            print('error: lathos hex string')
    return dec


def dec2hex(dec):
    '''
    dec2hex - Metatropi apo 10diko se 16diko
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
    hexStr = ''   # Gia athroisma
    # Pinakas gia metratropi se psifia tou 16dikou 0-15 se 0-9,A-F
    hexChars = ['0','1','2','3', '4','5','6','7', '8','9','a','b', 'c','d','e','f'];
 
    decSave = dec
    # Epanaliptiki diadikasia upoloipwn/diaireswn gia tin eyresi twn 16dikwn psifiwn se
    # anapodi seira 
    while dec > 0:
        hexDigit = dec % 16;   # 0-15
        hexStr = hexChars[hexDigit] + hexStr;  # Posthesi tis string stin arxi tou
                                               # prouparxontos gia na exoume anapodi seira
        dec = dec // 16;                       # Integer division
    return hexStr


def main():
    #==============================================
    # Eisagwgi enos 10dikou arithmou
    #==============================================
    decnum = int(input('Give a positive decimal number: '))
    hexStr = dec2hex(decnum)
    print('The hex for decimal {} is: {}'.format(decnum, hexStr))
    # Xrisi tis built-in function hex(decNumber)
    print('O hex tou 10dikou {} me tin python function einai: {}'
          .format(decnum, hex(decnum)))
    #==============================================
    # Eisagwgi enos string gia ton 16diko arithmo
    #==============================================
    hexString = input('Give a hex string: ')
    decnum = hex2dec(hexString)
    print('O 10dikos tou hex "{}" einai: {}'.format(hexString, decnum))
    # Xrisi tis built-in function int(str, base)
    print('O 10dikos tou hex "{}" me tin python function einai: {}'
          .format(hexString, int(hexString, 16)))


main()
