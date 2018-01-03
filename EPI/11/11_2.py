"""
11-2

0. T
sorted arr
search entry equal to its index

1. EX
[-2,0,2,3,6,7,9]
2 or 3

2. C
3. BF
iterate. O(N)

4. Qs
- invariant
sps index 2 has 2, in ex.
for any elem at right of 2,
either index == elem, like 3
or value exceeds index.
since sorted, will always exceed.

- if idx < val, skip rhs
- if ==, ret
- if >
idx is 1, val is 0.
since sorted, 
lhs is less.
max of one left is -1,
but idx is 0. induction.
so skip lhs

5. Out
while l < u:
    mid
    if mid < A[mid], u = mid -1
    > 
        l = mid + 1
    ==
        ret mid
ret -1
    
6. Edge
7. TS
T: n lg n
"""

def f(A):
    l, u = 0, len(A) - 1
    while l < u:
        m = l + (u - l) // 2
        if m < A[m]:
            u = m - 1
        elif m > A[m]:
            l = m + 1
        else:
            return m
    return -1

A = [-2,0,2,3,6,7,9]
print(f(A))
