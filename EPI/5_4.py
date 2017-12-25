# 5.4

def reachable(A):
    B = [False] * len(A)
    B[0] = True
    for i in range(len(A)):
        if B[i]:
            for j in range(i, i + A[i] + 1):
                if j < len(A):
                    B[j] = True

    if B[len(A) - 1] == True:
        return True
    return False

def reachable2(A):
    i, cur_max, end = 0, 0, len(A) - 1
    while i <= cur_max and i <= end:
        cur_max = max(cur_max, i + A[i])
        i += 1

    return cur_max >= end

A = [3, 3, 1, 0, 2, 0, 1]
print(reachable2(A))
B = [3, 2, 0,0,2,0,1]
print(reachable2(B))

