"""
10-1 merge sorted files

0. T
500 files
a - t since start of day
sorted by a
symbol, shares, price

arg: set of sorted seqs
ret: union of seqs as a sorted seq

1. C

2. EX
[3,5,7], [0,6], [0,6,28]
[0,0,3,5,6,6,7,28]

3. BF
sort combined
O(n lg n)

4. Qs
each is sorted.
smallest of k is min of all
append to res, get next from that list

- heap

- max or min?
min

- how to know which list the min came from?
tuple, (elem, listNo)

- if no more from a list?
ok. heap is smaller

5. Edge

6. Out
res = []
h = []
for idx, lst in enumerate(lists):
    h.append((lst[0], idx))
while h is not empty:
    min_elem, list_idx  = h.pop
    next_element = next(iters[list_idx], None)
    if next_elem is not None:
        push(h, (next, list_idx))

7. TS
O(n log k)
O(k)
"""
