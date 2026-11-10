"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # use a dict to record nodes has been copied
        # use dfs to append node's neighbors & check if it has been copied

        old_to_new = {}
        if not node:
            return None

        def dfs(node):
            # base case
            if node in old_to_new:
                return old_to_new[node]

            # new node to copy:
            clone = Node(node.val)

            # copy the node
            old_to_new[node] = clone # old -> new

            # clone its neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)
            


