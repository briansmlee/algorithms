"""
5-5

1. Task
delete duplicates in sorted arr

2. Clear

3. EX
arg: 2,3,5,5,7,11,11,11,13
ret: 2,3,5,7,11,13,0,0,0

4. BF
del() all repeats
O(N^2) due to copy over

Q: ok to overwrite?
yes. not using value later

5. Outline:
2 ptrs, i and j
add fst to A
for i from 1 to len A - 1
if i and i - 1 are equal, continue
else replace A[j] with A[i], and j++

O(N)
"""

def del_dups(A):
    i, j = 1, 1
    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            A[j] = A[i]
            j += 1
    
    for k in range(j, len(A)):
        A[k] = 0

A = [2,3,5,5,7,11,11,11,13]
del_dups(A)
print(A)
    



