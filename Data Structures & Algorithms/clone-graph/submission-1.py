"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # use dfs to explore neighbors, to append the neighbors, and check if the node is copied

        old_to_new = {} # use to stroe old node: new node to prevent from duplication 
        if not node:
            return None

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            clone = Node(node.val)
            old_to_new[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)




