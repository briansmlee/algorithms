"""
4.6 Successor

- Task
find next node, in-order successor of a given node
in BST
each node has link to its parent

- Q: in-order successor?
next node in inorder traversal of BST

- Q: how to find? depends on what?
go thru example
if right subtree exists, then leftmost/smallest elem in right subtree
if not and node is right child, go to parent until first the parent is left child. return it's parent.
if not and node is left child, subcase of 2.

- Outline
arg: node
ret: node or None

if node.right exists,
child = node.right
while child and child.right:
    child = child.right
return child

else
while node.parent and node.parent.right == node:
    node = node.parent
if node.parent.left == node:
    return node.parent
else
    return None
"""

def successor(node):
    if node.right:
        child = node.right
        while child and child.left:
            child = child.left
        return child

    else:
        while node.parent and node.parent.right == node:
            node = node.parent
        if node.parent.left == node:
            return node.parent
        else:
            return None

