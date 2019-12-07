def is_isogram(a):
    word = a.lower()
    les = []
    for letter in word:
        if letter.isalpha():
            if letter in les:
                return False
            les.append(letter)
    return True
is_isogran(a)
#An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
#Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

