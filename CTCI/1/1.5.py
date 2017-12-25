"""
CTCI 1.5 one away

3 types of edits can be performed on a string:
1. insert a char
2. delete a char
3. replace a char

given two strs, return if they are one edit or zero edits away.

-----
Q: consider 0 and 1 edit dist seperately?
may not be useful.

Q: by case. how to check if inserted a char?
- one is a char longer, let A be longer, B be shorter.
- A, B same until newly inserted char in A.
- if we skip that char in A, rest is same.

Q: deletion case?
- inverted.

Q: replace case?
- same len. let A, B
- same until replaced. skip both chars in A, B, then rest is same.

Q: immediate false cases?
- lens diff by more than 1

-----
steps:
- set A to be longer
- set is_diff to False. if true and new diff, return False
- compare chars in both
    - if diff, 1) check is_diff 2) increment depending on case 1 or 2.
"""

def is_one_away(A, B):
    len_diff = len(A) - len(B)
    if len_diff not in [-1, 0, 1]:
        return False
    
    if len(A) > len(B):
        A, B = B, A
    
    is_diff = False
    i, j = 0, 0

    while i < len(A):
        if A[i] != B[j]:
            if is_diff == True:
                return False
            else:
                is_diff = True

            if len(A) == len(B):
                i += 1
                j += 1
            else:
                j += 1

        else:
            i += 1
            j += 1 

    return True
    
A = 'pale'
B = 'ple'
print(is_one_away(A, B))
    
"""
Q: solution is dirty and long. How to clean up?
    




