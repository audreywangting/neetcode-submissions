from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        # 1. build the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = 0
        visited = set()


        # 2. dfs
        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # 3. count connected components
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)

        return count
