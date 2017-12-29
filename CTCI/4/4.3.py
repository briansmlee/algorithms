"""
4.3 List of Depths

Given
- binary tree

Task
- create linked list of all nodes at each depth

Assumptions
- use list as LL

Q: modify BFS?
- no need for visited array
- LL instaed of Q, one for each level
- for all elems in LL, insert children to new LL
- append old LL to list of LL, replace cur with new LL

Outline
lists
LL with root
while LL is not empty
for node in current LL,
append L,R children to new LL
append cur LL to lists
replace cur LL with new LL
"""

def list_of_depths(root):
    lists = []
    cur = [root]

    while len(cur) > 0:
        nxt = []
        for node in cur:
            if cur.left:
                nxt.append(cur.left)
            if cur.right:
                nxt.append(cur.right)
        lists.append(cur)
        cur = nxt

    return lists



        

