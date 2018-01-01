
def partition(pivot_index, A):
    # keep key
    A[pivot_index], A[0] = A[0], A[pivot_index]
    key = A[0]

    # index to less, equal, greater
    l, e, g = 0, 1, len(A) - 1

    # loop
    while e <= g:
        if A[e] < key:
            A[l], A[e] = A[e], A[l]
            l += 1
            e += 1
        elif A[e] == key:
            e += 1
        else:
            A[g], A[e] = A[e], A[g]
            g -= 1

# Test
A = [0,1,2,0,2,1,1]
print(A)
partition(2, A)
print(A) 
