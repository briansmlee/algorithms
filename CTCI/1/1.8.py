"""
1.8 Zero Matrix

Task:
- if an element in an M x N mtx is 0, its entire row and col are set to 0

Q: how many 0's in original?
- assume any num
- if many 0s, may repeat work.

Q: Brute Force?
- iterate thru all elems O(M * N)
- if 0, replace(). O(max(M, N)), say O(M)

Q: how fast?
- each replace() is O(N) 
- entire matrix, if BF, is O(M * (M * N))

Q: faster ways?
- do work afterwards, keep track of all M, N where 0 exist.
- O(MN)
- can't think of faster

Outline:
- temp of row(M), col(N)
- 1st: for each, if 0, mark temps
- 2nd: for each, if either is True, set to 0
"""

# O(M * N)
def zero(A):
    M, N = len(A), len(A[0])
    row = [False for _ in range(M)]
    col = [False for _ in range(N)] 

    for i in range(M):
        for j in range(N):
            if A[i][j] == 0:
                row[i] = True
                col[j] = True

    for i in range(M):
        for j in range(N):
            if row[i] or col[j]:
                A[i][j] = 0

    return A


A = [
        [1, 2, 3, 4],
        [5, 0, 7, 8],
        [9, 10, 11, 12]
    ]
print(zero(A))
        
    

