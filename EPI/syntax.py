"""
--------------------
5. Array
--------------------

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


--------------------
6. Strings
--------------------
s[3]
len(s)
s + t
s[2:4]
s in t

s.strip()
s.startswith(prefix)
s.endswith(suffix)
'Hello,World'.split(',')    # returns an array
3 * '01'
','.join(['Hello', 'World'])    # can be any collection (ex. tuple)
s.tolower()
'Name {name}, Rank {rank}'.format(name='Brian', rank=3)

immutable!!!
s = s[1:]
s += '123' create new array

s.isalnum()

--------------------
8. Stack & Queue
--------------------
Stack:

s.append(e)
s[-1]   # IndexError if empty
s.pop() # "
len(s) == 0

Queue:

from collections import deque
q = deque('abc' or [0,1,2]) # both three items, any iterable
q.append(e)
q[0]
q.popleft()

--------------------
10. Heaps
--------------------
min-heap = root is min = children are larger

Time
-----
heapify:    n
insert:     log n
max/min:    1
delete max: log n
search for arbitrary key:   n

Syntax
-----
import heapq
heapq.heapify(L)        # turns L into a list, in-place
heapq.nlargest(k, L)    # k largest elems in L
or nsmallest
heapq.heappush(h, e)
heapq.heappop(h)        # smallest elem
heapq.heappushpop(h, a) # pushes a on heap, then pops smallest elem
e = h[0]                # returns smallest elem w/o pop

Tips
-----
- if need max-heap, insert negatives
- augment data to tuple (key, data)
- if need to keep index of lists, use iterator and enumerate()
lists_iters = [iter(x) for x in sorted_lists]
for idx, val in enumerate(lists):


