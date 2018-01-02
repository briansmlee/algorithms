"""
6.8 look and say sequence

0. T
arg: int n
ret: nth integer in the LAS seq

1. C
- nth integer?
nth element, which is integer, in sequence.

2. EX
n = 3 -> '21'

3. BF
- how to gen nth?
run-length encoding!

- iterative?
call helper n times
helper
takes str, ret new str
[]
count = 1
while same char, inc count
append str(count), char
''.join()

O(M), where m is len from prev in seq

4. Qs
- faster?
"""







