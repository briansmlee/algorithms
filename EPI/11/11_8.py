"""
11-8

0.T
find kth largest element in an array.

1.EX
[3,2,1,5,4]
3rd -> 0

2.C
3.BF
- search largest k times. O(nk)
- sort, return k-th. O(n lg n)
- heap
T: O(n lg k)
S: O(k)

4.Qs
- bsearch
choose x at random
partition
if |rhs| == k - 1, ret x
if num < k - 1, find k - 1 - num more in lhs.
if num > k - 1, in rhs, search for k again.

5.Out
rand int btw 
    
6.Edge
7.TS
T(n) = O(n) + T(n/2)
T(n) = O(n)
"""
import random

def kth_largest(A, k):
    def partition(l, r, p):
        p_val = A[p]
        A[p], A[r] = A[r], A[p]
        new_p = l
        for i in range (l, r):
            if p_val < A[i]:
                A[new_p], A[i] = A[i], A[new_p]
                new_p += 1
        A[new_p], A[r] = A[r], A[new_p]
        return new_p
   
    l, r = 0, len(A) - 1
    while l <= r: 
        rand_p = random.randint(l, r)
        p = partition(l, r, rand_p)
        if p > k - 1:
            r = p - 1
        elif p < k - 1:
            l = p + 1
        else:
            return A[p]
    return None 

A = [3,2,1,5,4]
print(kth_largest(A, 1))
print(kth_largest(A, 2))
print(kth_largest(A, 3))
print(kth_largest(A, 4))
print(kth_largest(A, 5))



