# subset of size k

def subset(A, k):
    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]

    return A[:k]

