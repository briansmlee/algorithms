import string

# reverse all words in a sentance

# Assumptions:
# 1. number of spaces?
# 2. can't use built-ins?

def f(s):
    return ' '.join(list(reversed(s.split(' '))))

def f1(s):
    # reverse all
    s = s[::-1]

    def reverse_word(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    start = 0
    i = 0
    while i < len(s) - 1:
        if s[i] == ' ':
            end = i - 1
            reverse_word(s, start, end)
            # skip all adj spaces
            while s[i] == ' ':
                i += 1
                start = i
        
        else:
            i += 1

    # rev last word
    reverse_word(s, start, len(s) - 1)
    return s
        
        

s = 'Alice likes Bob'
print(f(s))

s1 = 'Alice   likes  Bob oppa'
print(f1(s1)) 
    


