
# preorder traversal

def f(tree):
    res = []
    cur = collections.deque([tree])
    while cur:
        nxt = collections.deque([])
        cur_list = []
        while cur:
            node = cur.popleft()
            if node:
                cur_list.append(node.data)
            nxt += [node.left, node.right]
            # nxt.append(node.left)
            # nxt.append(node.right)
        res += cur_list
        nxt = cur
    
    return res
