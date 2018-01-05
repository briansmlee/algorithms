"""
11-3

0.T
cyclically sorted if
shift entries so that it is sorted.
design O(lg n) algo for finding pos of smallest elem in cyclical sorted arr.
all elems are distinct

1.EX
2.C
3.BF
- findmin
- find fst and only pair s.t. val dec
O(N)

4.Qs
- given an arbitrary index, possible to elim half?
- inc/dec? no.
- by value?
since circular, fst and last are close.
if fst and lst are "mid" values, min should exist to left.

- try regular bsearch. what to search?
get mid. either mid is before min or after min.
if mid is before min, elim lhs.
else, elim rhs

- how to cmpr mid and min in O(1)?
compare with fst/lst (the circular break pt)
either fst < mid or >.
if fst < mid, mid is in increasing portion of arr. LHS not contain min. look RHS.
if >, look LHS. 


5.Out
6.Edge
7.TS
"""
