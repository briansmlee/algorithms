# increment an arbitrary precision integer

def increment(A):
    inc = 1
    i = len(A) - 1 
    while inc and i > 0:
        if A[i] == 9:
            A[i] = 0
        else:
            A[i] += 1
            inc = 0
        i -= 1

    # case 0
    if inc and A[0] == 9:
        A[0] = 0
        A.insert(0, 1)

    return A

def increment1(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        else:
            A[i] = 0
            A[i - 1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0) # nice
    
    return A
        
