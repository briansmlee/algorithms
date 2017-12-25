# palindrome permutation

"""
1. 
O(N)
implementation is wrong
b/c a str is palindrome permutation iff
no more than one character has odd count!
def f(A):
    count = [0] * 26
    for char in A:
        index = ord(char) - ord('a')
        if 0 < index and index < 26:
            count[index] += 1

    for e in count:
        if e != 0 and e % 2 == 0:
            return False

    return True
            
A = 'Tact Coa'
print(f(A))

2.
str is permutation of palindrome iff
no more than one character has odd count.
steps:
- init arr of all alphabets (not ASCII!)
- for each char in str, inc count in arr
- for each elem in arr, if more than one is odd, false.
- True
"""
def f(A):
    arr = [0] * 26
    for c in A:
        index = ord(c.lower()) - ord('a')
        if 0 <= index and index <= 25:
            arr[index] += 1
    
    odd_exists = False
    for e in arr:
        if e % 2 == 1:
            if odd_exists == False:
                odd_exists = True
            else:
                return False

    return True

A = 'Tact Coa'
print(f(A))
