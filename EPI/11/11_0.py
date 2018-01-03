"""
implement binary search

while True:
if L > U, ret None
mid
compare
l or r

"""

def bsearch(key, A):
    L, U = 0, len(A) - 1
    while L <= U:
        mid = L + (U - L) // 2
        if A[mid] > key:
            U = mid - 1
        elif A[mid] < key:
            L = mid + 1
        else:
            return mid
    return -1

