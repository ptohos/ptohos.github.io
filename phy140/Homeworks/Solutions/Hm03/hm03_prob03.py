#!/usr/bin/python3

gene = 'AGTCAATGGAATAGGCCAAGCGAATATTTGGGCTACCA'

def freq(letter, text):
    counter = 0
    for i in text:
        if i == letter :
            counter += 1
    return counter/len(text)

def pairs(letter, text):
    counter = 0
    for i in range(len(text)):
        if i < len(text) - 1 and \
           text[i] == letter and \
           text[i+1] == letter :
            counter += 1
    return counter

def mystruct(text):
    counter = 0
    for i in range(len(text)):
        # Ereyna gia tin uparksi tis sygkekrimenis domis
        # ksekinontas apo ti thesi i sto string text
        if text[i] == 'G':
            print('Found G at position %d'%i)
            # Ereyna anamesa sta grammata A and T
            j = i + 1
            pattern_start_pos = j
            while text[j] == 'A' or text[j] == 'T' :
                print('next letter is ok! Got a:%s' % text[j])
                j += 1
            print('ending of pattern is %s' % text[j:j+2])
            if text[j:j+2] == 'GG' :
                pattern_stop_pos = j+1
                # Swstos termatismos tis seiras kai otan yparxoun
                # perissotero apo 2 chars sto pattern, diaforetika
                # mporei na vrei 2 diadoxika GG 
                if pattern_stop_pos - pattern_start_pos > 2:
                    counter += 1
                    print('Got a pattern between positions [%d,%d]:%s' % \
                          (pattern_start_pos,pattern_stop_pos, \
                           text[pattern_start_pos:pattern_stop_pos+1]))
    return counter

print('Frequency of C: %.1f' % freq('C',gene))
print('Frequency of G: %.1f' % freq('G',gene))
print('Number of AA pairs: %d' % pairs('A',gene))
print('Number of structures: %d' % mystruct(gene))


      
                  
    
