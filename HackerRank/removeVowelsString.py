import unittest

def removeVowels(s):
    s = list(filter(lambda x: not is_vowel(x), list(s)))
    return ''.join(s)

def is_vowel(s):
    if s == 'a' or s =='e' or s == 'i' or s == 'o' or s == 'u':
        return True
    return False 

