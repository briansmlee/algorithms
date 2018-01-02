"""
10-0 k longest strings

0. T
takes sequence of strs in streamig fashion
return k longest strings
no need to order the strings

1. C

2. EX
arg ['a', 'bbb', 'cc', 'dddd'], 2
ret ['bbb', 'dddd']

3. BF
- sort, return last k

4. Qs
- heap
- minmax?
min
- sz?
k
- when to insert?
if heap less than k
if min among k longest is less than new, remove min and insert new

5. Cor

6. O
h = []
for s in stream:
    if len(h) < k, hq.heappush(h, s)
    elif len(h[0]) < len(s), pop, push(h, s)
return h

7. TS
T: O(n log k)
S: O(k)
"""


