"""
5.18 spiral ordering

1. Task
arg: 2d arr
ret: 1d spiral ordering

2. clarify

3. EX

4. BF

Q: layers?

Q: how to specify a layer?

Q: how to iterate thru a layer?
4 eql sized subparts
sps layer 1
A[1][1] to A[1][end - 1 - 1]
A[1][end - 1] to A[end - 1 - 1][end - 1]
A[end - 1][end - 1] to A[end - 1][1 + 1]
A[end - 1][1] to A[end - 1][1 + 1]

5. Outline
ordering = []

def helper(n)
iterate thru 4 suparts,
adding to ordering

ret order

O(n^2)
"""

def spiral(A):
    
    def layer(A, n, order):
        for i in range(n, len(A) - n):
            order.append(A[n][i])
        for i in range(n + 1, len(A) - n - 1):
            order.append(A[i][len(A) - n - 1])
        for i in reversed(range(n, len(A) - n)):
            order.append(A[len(A) - n - 1][i])
        for i in reversed(range(n + 1, len(A) - n - 1)):
            order.append(A[i][n])
    
    order = []
    mid = len(A) // 2
    for l in range(mid):
        layer(A, l, order)
    if len(A) % 2 == 1:
        order.append(A[mid][mid])
    
    return order

A = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral(A))
