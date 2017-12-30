"""
4.4 check balanced

- Task
check if binary tree is balanced, that is 
heights of two subtrees of any node never differ by more than one

- BF
for all nodes, check heights of subtree
if height() is O(lg n), O(n lg n)

- Q: find heights of all nodes from bottom up?
height() will take O(1), since comparing L and R

- Q: Recursive?
return value is height

- Q: if R and L heights are not equal, cannot quit recursion
set global is_balanced variable
is checking only root balance ok?

- Q: root is unbalanced iff any is unbalanced?
No. consider symmetrically unbalanced tree

- Outline
global is_balanced variable = True
helper takes a node
recurses into L and R,
compares height ret value
if diff by more than 1, set is_bal to False
return max height.
"""

def check_balanced(root):
    is_balanced = True
    
    def check_subtree(node):
        if not node.left and not node.right:
            return 1

        h1 = check_subtree(node.left)
        h2 = check_subtree(node.right)

        if abs(h1 - h2) > 1:
            is_balanced = False

        return max(h1, h2) + 1

    check_subtree(root)
    return is_balanced

"""
- Note
this soltuion will not work, since is_balanced is local every recursive call.
instead, pass error code as the return value of the recursive func.
"""
