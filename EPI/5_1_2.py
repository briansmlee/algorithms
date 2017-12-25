
def partition(A, i):
    a, b, c = 0, 0, len(A)
    pivot = A[i]
    while b < c:
        cur = A[b]
        if pivot == cur:
            b += 1
        elif cur < pivot:
            A[a], A[b] = A[b], A[a]
            a += 1
            b += 1
        else:
            c -= 1
            A[c], A[b] = A[b], A[c]
    
    return A

A = [0, 1, 2, 0, 2, 1, 1]
partition(A, 3)
print(A)

