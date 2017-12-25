# 1.3 URLify

"""
again, wrong assumption.
by "true" length of the string,
means length of the original string
with extra spaces removed.

def urlify(A, n):
    
    B = ['a' for _ in n]
    j = 0
    for c in A:
        if c == ' ':
            B[j], B[j+1], B[j+2] = '%', '2', '0'
            j += 3
        else:
            B[j] = c
            j += 1
    return B
"""

# hint: modify string from backwards

def urlify(arr, n):
    A = list(arr)
    # i,j point to end of old, new strings
    end = j = len(A) - 1
    while A[end] == ' ':
        end -= 1
    
    for i in reversed(range(end + 1)):
        if A[i] == ' ':
            A[j - 2], A[j - 1], A[j] = '%', '2', '0'
            j -= 3
        else:
            A[j] = A[i]
            j -= 1

    return ''.join(A)

A = "Mr John Smith    "
n = 13
B = urlify(A, n)
print(B)

"""
NOTE:
*** 1. TRAVERSE FROM BACK, IF OVERWRITE IS OK.
2. I assumed that the terminal spaces fit the string exactly.
if not, count # of spaces to count exact # of spaces needed.
*** 3. string is immutable in python.
    so, more sense to start with list of chars, for this in-place algo.
"""
            
            
