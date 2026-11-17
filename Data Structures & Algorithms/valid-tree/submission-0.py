from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # define valid tree: connected + acyclic
        # 1. check len(edge) == # of node - 1
        # 2. use dfs/bfs to make sure all nodes are connected


        # 1. len(egde) must == n-1
        if len(edges) != n-1:
            return False


        # 2. build adjacency list
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 3. DFS
        visited = set()
        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)

        # 4. check if connected
        return len(visited) == n