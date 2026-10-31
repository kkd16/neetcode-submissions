"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        seen = {}

        # stops when node is seen already
        def dfs(node):
            if node in seen:
                return seen[node]
        
            copy = Node(node.val)
        
            seen[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node)

        


        