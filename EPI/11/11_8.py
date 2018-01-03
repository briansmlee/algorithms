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
def help(hi, lo, k):
    x = rand
    partition(A, x), and get idx of x.
    if len(A) - idx == k, ret true
    if >, lo = idx + 1 # more than k. rhs. 
    if <, hi = idx - 1 # less than k. lhs, k -= len(A) - idx
    
    
6.Edge
7.TS
"""


