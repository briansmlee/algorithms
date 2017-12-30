"""
4.5 validate BST

- Task
check if a binary tree
is a binary search tree

- Assumptions
BST property: for all node, left <= node.data < right
no node is inf or -inf

- BF
for every node, check if the BST property is true.
if start from top, repeating work.
recursively?

- Q: if L and R subtree satisfy BST prop, then only check three nodes?
No.
in Left subtree, the largest elem might be larger than root.
in R same idea
b/c a recursive func does not know if root will be left or right child of its parent,
must keep info of both max and min

- Outline
recursive helper
arg: node
ret: (min, max)

1. error case
if (inf, -inf), return same

2. if neither, (node, node)
3. if only one, still compare other, and fill missing with node.

recursive:
call on left, right
if l_max > node, ret (inf, -inf)
if r_min < node, (inf, -inf)

return (l_min, r_max)

- complexity
at each call, O(1) time
called for every node.
O(n)
"""

def validate_BST(root):

    def validate(node):
        if node.left:
            (l_min, l_max) = validate(node.left)
            if l_max > node.data:
                return (float('-inf'), float('inf'))
            else:
                ret_min = l_min
        else:
            ret_min = node.data
            
        
        if node.right:
            (r_min, r_max) = validate(node.right)
            if r_min < node.data:
                return (float('-inf'), float('inf'))
            else:
                ret_max = r_max
        else:
            ret_max = node.data

    if validate(root) == (float('-inf'), float('inf')):
        return False
    else:
        return True
            

        

