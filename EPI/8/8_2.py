"""
8-2 Evaluate RPN expression

0. T

1. C
invalid input?

2. EX
2 3 + 4 5 x x

3. BF
find outermost expr
and recurse

4. Qs
- stack?
iter from l to r
push base case
if operator, pop two and compute
push result

5. O
"""

