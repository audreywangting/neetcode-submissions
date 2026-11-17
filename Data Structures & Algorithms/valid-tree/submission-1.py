from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # unidirected, use dfs to explore if nodes are connected
        # valid tree: connected & no cycle

        # 0. there must be only n-1 edges for the tree (not a cycle)
        if len(edges) != n-1:
            return False

        # 1. build adjacency list - to quickly know dependency
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        # 2. dfs
        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(0)

        return len(visited) == n

