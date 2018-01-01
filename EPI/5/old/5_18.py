
# spiral ordering of 2D array

def spiral(A):
    n = len(A)
    # base cases
    if n == 0:
        return []
    
    if n == 1:
        return [A[0][0]]
    
    # store while traversing outer
    res = []
    res += A[0]
    for j in range(1, n - 1):
        res.append(A[j][n-1])
    res += list(reversed(A[n - 1]))
    for j in reversed(range(1, n - 1)):
        res.append(A[j][0])
   
    # return cur + recursive call
    return res + spiral([row[1:-1] for row in A[1:-1]])

A = [[1, 2, 3], [4,5,6], [7,8,9]]
print(spiral(A))

B = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiral(B))
        
        
        

