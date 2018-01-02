"""
8-6 compute binary tree nodes in order of increasing depth

0. T
arg: binary tree
ret: array consisting of keys at same lvl

1. C
- breaking ties from left to right?
order.

2. EX
given

3. BF

4. Qs
- BFS?
after each lvl, must add to return arr

5. O
res = []
cur = deque([root])
is_rev = False
while cur not empty:
    nxt = deque()
    for node in cur:
        append node.l and r to nxt, if they exist
    if is_rev:
        cur.reverse()
    is_rev = not is_rev
    append cur to res
    cur = nxt
"""

    
