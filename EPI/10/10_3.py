"""
10-3 sort almost-sorted array

0. T
arg: arr of nums
ret: -
print nums in sorted order
each num is at most k away from its correctly sorted pos
i.e k-sorted

1. EX
[3,-1,2,6,4,5,8], 2-sorted
 -1,2,3,4,5,6,8
    
2. C

3. BF
sort
O(n lg n)

4. Qs
sps we keep a subset,
and select min.

- smaller may be added later.
- how big a subset?
sps fill index i. 
then, correct elem must be at least in index i + k
so, k + 1, if we assume empty at start

- empty at start of iteration?
no.
but, after idx 0 (heap of 3), 
we pop 1.
to find min for idx 1,
push one, pop one.
so, max size k + 1

- min heap

5. Edge
- start?
make heap with k init elems.

6. Out
h = []
fill with first k + 1
i = k + 1
while h is not empty
    print h.pop()
    if i < len(A)
        h.push(h[i])
    i += 1

7. TS
T: n lg k
S: k
"""
