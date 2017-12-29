"""
4.1 Route Between Nodes

Task
- directed graph
- if there exists route between two nodes

Q: BF
- BFS on n1, if n2 is seen, return true. else, false.
- O(|V| + |E|) 

Q: when to return T
- 

Q: faster?
- consider bidirectional search
- since directed, given n2, must find all nodes that have edges going to n2.
- if adj list, hard (more time). if matrix, same time.

Q: graph representation

BFS sol Outline:
- q, visited
- insert n1 to q
- mark n1 visited
- while q is not empty,
- popleft
- for all adj nodes
- if n2, return True
- if not visited, enq 
"""

from graph import graph
from collections import deque

def route(G, n1, n2):
    def to_idx(c):
        return ord(c) - ord('A')

    q = deque()
    visited = [False for _ in range(6)] # from example graph

    q.append(n1)
    visited[to_idx(n1)] = True
    
    while len(q) != 0:
        cur = q.popleft()
        for node in graph[cur]:
            if node == n2:
                return True
            if not visited[to_idx(node)]:
                visited[to_idx(node)] = True
                q.append(node)

    return False

print(route(graph, 'E', 'C')) # T
print(route(graph, 'A', 'E')) # F
