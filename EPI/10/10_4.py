"""
10-4 k closest stars

0. T
earth is at 0, 0, 0
star = pt
dist = light yrs
10^12 stars

find k stars closest to earth

1. EX
2. C
- assume dist() is given

3. BF
sort

4. Qs
- max heap?
k closest. cmpr longest among those.
insert -dist
- if max > new, pop max, insert new.
- keep dist info?
have to, since heap.
(dist, star)
- 

5. Edge
- start?
start with first k

- if same dist?
not replace.

6. Out
same

7. TS
same
"""

