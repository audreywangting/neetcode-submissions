class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find: undirected graph, connected

        # 1. initialize parent as itself
        # 2. find function: find its root
        # 3. union: if not connected: return True and connect, if connected: return False
        # 4. iterate all edges to check not unoin: already connected but still edge >> cycle detected

        n = len(edges)
        parent = [i for i in range(n+1)]

        def find(x):
            while x != parent[x]: # keep searching for the parent
                x = parent[x]

            return x

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            
            parent[root_y] = root_x
            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]