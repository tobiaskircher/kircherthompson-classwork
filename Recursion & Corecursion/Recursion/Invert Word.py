def flip_word(word):
    n = len(word)
    if n == 1:
        return word[0]
    else:
        return flip_word(word[1:]) + word[0]


word = input("Word:") 
print("\nWord Reversed:")
print(flip_word(word))
