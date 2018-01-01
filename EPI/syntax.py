"""
5. Array

[3, 5, 7]
[1] + [0] * 10
list(range(100))
len(A)
A.append(42)
A.remove(42)
A.insert(3, 28)
a in A

B = A vs B = list(A)
copy.copy(A) vs copy.deepcopy(A)

min(A), max(A)

bisect.bisect(A, 6)
bisect.bisect_left(A, 6)    # locates index in A to insert 6. left if 6 already exists.
bisect.bisect_right(A, 6)

A.reverse() # in-place
reversed(A) # returns iterator
A.sort()    # in-place
sorted(A)   # returns copy

del A[i]
del A[i:j]

A[i:j:k]
# all index n s.t. i <= n < j
# in i, j, -1 is last element, -2 is one before last, ...
# in k, -2 goes from the back to front
A[::-1]         # reverses the list
A[k:] + A[:k]   # rotates list by k to the left
B = A[:]        # shallow copy

list comprehension
1. input seq
2. iterator over input seq
3. logical condition over the iterator
4. expr that yields elems of derived list
+ multiple lvls of looping






