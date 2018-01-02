"""
10-2 Sort an inc-dec array

0. T
k-inc-dec = inc upto certain index after which they dec, 
repeat k times
sort k-inc-dec arr

1. C
- repeats?

2. EX
4-inc-dec

3. BF
sort whole thing
O(n lg n)

4. Qs
- given m smallest, how to find m + 1th smallest?
if rev dec seq, have k inc seqs
can only consider k current smallest
- heap
- sz?
k
- min/max?
min
- iterator?
- keep which list cur min is from?
tuple, (elem, idx)

- how to rev each dec seq?
is_inc = True
arrs = []
start, end
while start < len(A)
if is_inc
    while end + 1 < len(A) and A[end] < A[end+1]
        end += 1
    arrs.append(A[start:end])
    is_inc = F
    start = end = end + 1
else
    opposite

5. Edge
- inflection pts
dec seq takes inf pt

6. Out
do above,
do 10-1

7. TS
T: O(n log k)
S: O(k)
"""
