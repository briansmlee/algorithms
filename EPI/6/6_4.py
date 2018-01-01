"""
6-4 replace and remove

1. T
given an arr of chars and integer-valued size for valid
- replace 'a' by two 'd's
- delete each entry containing a 'b'

2. C
in-place? Y

3. EX
[a,c,d,b,b,c,a] to [d,d,c,d,c,d,d]
[a,b,a,c,_] to [d,d,d,d,c]

4. BF
del each a, insert two 'd's
del each b
O(N * M), M is # |a| + |b|


if start from front, can't overwrite due to 'd's
so, start from back

let i, j be ptrs to end of old and new strings
j must start at exactly the end.
do a run, and count.

as i iterates backwards,
fill j by three cases.

loop will NOT overwrite any neccesary info,
since i < j until 0.
"""


