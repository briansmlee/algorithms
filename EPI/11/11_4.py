"""
11-4

0.T
arg: nonneg int
ret: largest int whose sqaure is < = int.

1.EX
16 -> 4
300 -> 17

2.C

3.BF
compute sqr upto. O(n^(1/2))

4.Qs
- just sqrt and floor? 
not allowed.

- bsearch 1 to n?

- geq?
try x.
if x^2 < a, might be the best. still look rhs.
if >, x is too big. skip rhs.
if ==, best.

- x^2 < a
update as cur best
do bsearch on rhs

5.Out
6.Edge
- init hi with 1?

7.TS
"""
def int_sqrt(n):
    lo, hi, res = 0, n, -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if mid**2 < n:
            res = mid
            lo = mid + 1
        elif mid**2 > n:
            hi = mid - 1
        else:
            return mid
    return res

print(int_sqrt(300))

"""
Note:
- no need to use the res field!
keep invariant:
let n in l <= n <= r be 
all nums s.t. unexamined or its sqr is strictly greater than x.
"""

