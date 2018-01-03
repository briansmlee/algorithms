"""
11-1 first occurrence of k

0. T
1. EX
2. C
3. BF
iterate thru. O(N)

4. Qs
- sorted
if less than certain pt, no need to look at rhs

- if match
same elem can be at lhs
must check lhs

- sps checked lhs, now less than key.
rhs

- which condition is change?
key > mid, same
key < mid, same

- if key = mid, 
check lhs.
if key not in lhs, return cur mid

- recursive
- rec also if key > mid, key < mid?
sure

5. Out
6. Edge
7. TS
T: n lg n
"""

def f(key, A):
    
    def h(start, end):
        if start > end:
            return -1
        mid = start + (end - start) // 2
        if key < A[mid]:
            return h(start, mid - 1)
        elif A[mid] < key:
            return h(mid + 1, end)
        else:
            res = h(start, mid - 1)
            if res < 0:
                return mid
            else:
                return res 

    return h(0, len(A) - 1)

A = [-14,-10,2,108,108,243,285,285,285,401]
print(f(108, A), f(285, A))

"""
Note:
- instead of recursive, keep a field/var
that maintains leftmost occurence of the key seen so far.
""" 
                
        
