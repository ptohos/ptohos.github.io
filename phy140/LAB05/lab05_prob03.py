brit_word = 'flavour'
amer_word = brit_word[:5] + brit_word[6:]
print(amer_word)

# alternative
amer_word = brit_word.replace('u','')
print(amer_word)

