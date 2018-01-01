"""
5-0

1. task
arg: arr of ints. 
reorder s.t. even appear first

2. clarify

3. BF
do until no even found
find first even num, swap with first elem.
O(n^2)

Hint: operate from both ends?
ptrs to L and R
while L < R
L   R   index
O   O   R--
O   E   swap
E   O   L++ R--
E   E   L++

move ptrs until L has odd and R has even.
if A[L] is even, L++, cont
if A[R] is odd, R--, cont
swap
L++ and R--

O(N)
"""

def reorder(A):
    L, R = 0, len(A) - 1
    while L < R:
        if A[L] % 2 == 0:
            L += 1
            continue
        if A[R] % 2 == 1:
            R -= 1
            continue
        A[L], A[R] = A[R], A[L]
        L += 1
        R += 1


