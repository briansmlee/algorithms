"""
4.2 Minimal Tree

Task
- given sorted array
- unique int elems
- create BST
- with minimal height

Q: insert middle?
- a <= n < b, |a| ~ |b|
- true for every node
- recursively
- n log n

Q: what is given?
- BST class
- insert

Outline
- given A, BST
- middles inserted before L or R
- preorder
- if recursive, need start and end
"""

def minimal_tree(A):
    def helper(A, BST, start, end):
        if start > end:
            return None

        # if start == end:
        #    BST.insert(A[start])
        #   return

        mid = (start + end) / 2
        BST.insert(A[mid])
        helper(A, BST, start, mid - 1)
        helper(A, BST, mid + 1, end)
    
    BST = BST()
    helper(A, BST, 0, len(A) - 1)

    return BST

"""
NOTE
1. base case handling
2. insert() is wrong! we are adding to the prev node itself.
"""

class TreeNode():
    left = None
    right = None

    def __init__(self, d):
        self.data = d
    
def minimal_tree1(A):
    def f(A, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        node = TreeNode(mid)
        node.left = f(A, start, mid - 1)
        node.right = f(A, mid + 1, end)
        return node
    
    return f(A, 0, len(A) - 1)

A = [0,1,2,3,4,5,6]
node = root = minimal_tree1(A)
while node is not None:
    print(node.data)
    node = node.right
    
    

    

