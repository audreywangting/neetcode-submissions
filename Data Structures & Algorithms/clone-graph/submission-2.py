"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # old_to_new dict to keep all copied nodes, w/o duplication
            # old: new
        # dfs: explore, append all neighbors, check duplications

        old_to_new = {}
        if not node:
            return None

        def dfs(node):
            # check duplication
            if node in old_to_new:
                return old_to_new[node]
            
            # start copying
            clone = Node(node.val)
            old_to_new[node] = clone

            # append neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)


            
