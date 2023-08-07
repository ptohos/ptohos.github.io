#!/usr/bin/python3


lst= (["deer", "net", "ten", "reed", "refer", "raw", "war", 
       "addition", "frequency", "platform", "according"])
 
words={}
def find_opposites(lst):
    new_lst =[] 
    for word in lst : 
        rev_word = word[::-1]             # Anapoda i leksi
        if word == rev_word:
            print("Palindrome: ",word)
            continue    # Palindromo
        if rev_word in lst:
            words[word]=words.get(word,0)+1
            words[rev_word]=words.get(rev_word,0)+1
            if words[word]==1 and words[rev_word]==1:
                new_lst.append((word,rev_word))
    return new_lst
 
print(find_opposites(lst))
