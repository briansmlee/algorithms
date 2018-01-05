"""
11-6

0.T
arg: 2D array sorted, rows/cols nondec
arg: num
ret: if num appears in 2D

1.EX
2.C
3.BF
- iterate. O(n^2)

4.Qs
sps choose a pt
if pt < target
all in Q2 is less. elim.
if pt > t, elim Q4

- after elim, how to choose nxt pt to test?
elims most num of pts.

- in diag?
find largest int leq target in diag.
elim Q2, examine rest.
O(n^2)

- subproblems?
if div by 4 squares, all are sorted.
create 3 subp's of sz 1/4 each.

- bsearch in each row.
n log n

- O(n)?
elim a row or col per iteration.
let a = A[0][n-1]
a is largest of row 0, smallest of col n-1
if a < x, row 0 does not contain x. move 1 down.
if a >= x, col n-1 ". move 1 left.
same problem.

- end?
if out of index

5.Edge
6.Out
7.Ts
"""
