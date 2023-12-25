#Function that detect pangram or not, return True or False
#A pangram is a sentence that contains every single letter of the alphabet at least once.
def is_pangram(str):
    #your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    str = str.lower()
    for i in alphabet:
        if i not in str:
            return False
        return True
    
#refactored
def is_pangram(str):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(str.lower())

#test
print(is_pangram("The quick, brown fox jumps over the lazy dog!")) # True
print(is_pangram("This is not a pangram.")) # False
print(is_pangram("Cwm fjord bank glyphs vext quiz")) # True
