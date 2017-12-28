"""
3.5 Sort Stack

Task
- sort a stack s.t. smallest items are on top.
- use one additional stack only.

Assume
- assume we can use O(1) storage

Q: loop invariant?
- say s2 is sorted, and s1 has unsorted elems

Q: how to insert an elem in s1 to s2?
- keep elem in tmp
- pop s2 until elem > s2
- push elem, then push back the popped s2.

Q: time?
- O(N^2)

Q: faster?


Outline:
- init empty s2
- counter for popped items from s2
- for each elem in s1, do as above.
"""

def sort_stack(s1):
    s2 = []
    
    while len(s1) != 0:
        s2.append(s1.pop())
    
    while len(s2) != 0:
        count = 0
        tmp = s2.pop()

        while len(s1) != 0 and s1[-1] < tmp:
            s2.append(s1.pop())
            count += 1
        
        s1.append(tmp)

        for i in range(count):
            s1.append(s2.pop())


s1 = [3, 5, 2, 1]
sort_stack(s1)
print(s1)
    
