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

- Q: how to do this?
recursive


