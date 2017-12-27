"""
CTCI 1.7 Rotate Matrix

Task:
- N x N matrix
- each pixel is 4B
- rotate by 90 deg, assume clockwise
- in place?

Q: where does A[i][j] go in B?
- A[0][0] -> A[0][-1] -> A[-1][-1] -> A[-1][0]

Hint: think layers

Q: how to rotate a layer?
- divide a layer into four equal parts (row minus last)
- replace each part  with prev
- keep first part in temp
- 4->1, 3->4, ...

Q: indexing problem? rows vs cols
- given a layer, what to do is same.
- helper function takes layer

Layout:
- helper function takes size of elems in layer
- temp of n-1
- copy part 1 to temp
- 4->1 ...
- iterate over all layers

details:
- input to helper? what is n?
"""


"""
skipped implementation,
come back later.

def rotate(M):
    def rotate_layer(M, n):
        length = len(M) - n * 2
        temp = []
        
        for j in range(n, len(M) - n):
            temp.append(M[n][j])
        for 

    for i in range(len(M) / 2):
        rotate_layer(i)
"""
