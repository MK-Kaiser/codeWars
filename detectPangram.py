'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

import string

def is_pangram(s):
    alpha = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 
             'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    for c in s.lower():
        if c in alpha.keys():
            alpha[c] = alpha.get(c, 0) + 1
    if 0 not in alpha.values():
        return True
    else:    
        return False
        
        
pangram = "The quick, brown fox jumps over the lazy dog!"
Test.assert_equals(is_pangram(pangram), True)
