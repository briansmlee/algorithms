"""
10-6 k largest elems in max-heap

0. T
given max heap, represented as array A, 
compute k largest elems in the max heap.
cannot modify the heap.

1. EX

2. C
- copy ok?

3. BF
copy, then extract k times.
k log n

4. Qs
- use heap property?
complete binary tree
1,2,4,8,16...

- if k is 3 < k < 7, no need to look below?
No.

- if k is 3, no need to look below 3rd layer.

- no need to look below sth that is still in heap!
number of items we have to examine are 1,2,3,4,...
replace max among those with 2 new items.


5. Edge

6. Out

7. TS
k log k?
"""
