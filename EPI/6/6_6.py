"""
6-6 reverse all words in sentence

0. T
arg: set of words sep by whitespace

the order of words are reversed

1. C

2. EX
'Bob likes Alice' -> 'Alice likes Bob'

3. BF
complex

4. Qs
consider two steps:
    1. reverse entire sentence
    2. reverse each word

Q: order and num of spaces?
also reversed

Q: how to rev each word?
skip blanks. find new start
find end of word.
reverse

while start < len(A):
    while A[start] == ' ':
        start, end = start + 1, end + 1
    while A[end] and A[end] != ' ':
        end += 1 # one past
    reverse(A, start, end - 1)
    start = end

O(n)
"""

def reverse_words(s):
    def rev(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1

    rev(s, 0, len(s) - 1)
    start = end = 0
    while start < len(s):
        while s[start] == ' ':
            start, end = start + 1, end + 1
        while end < len(s) and s[end] != ' ':
            end += 1
        rev(s, start, end - 1)
        start = end

s = ['B','o','b',' ','l','i','k','e','s',' ','A','l','i','c','e']
reverse_words(s)
print(s)
