"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = set()
        d = defaultdict(Node)
        queue = [node]
        while queue:
            n = queue.pop(0)
            if n in visited:
                continue
            visited.add(n)
            if n.val not in d:
                d[n.val] = Node(n.val,[])
            n1 = d[n.val]
            for n2 in n.neighbors:
                if n2.val not in d:
                    d[n2.val] = Node(n2.val,[])
                n1.neighbors.append(d[n2.val])
                if n2 not in visited:
                    queue.append(n2)
        return d[node.val]
