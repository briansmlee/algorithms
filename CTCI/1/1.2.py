# 1.2 check permutation

def is_permutation(A, B):
    if len(A) != len(B):
        return False

    count = [0 for _ in range(128)]
    for a in A:
        count[ord(a)] += 1
    for b in B:
        count[ord(b)] -= 1
    for c in count:
        if c != 0:
            return False

    return True


A = "hello"
B = "olleh"
C = "bye"
print(is_permutation(A, B))
print(is_permutation(A, C))

