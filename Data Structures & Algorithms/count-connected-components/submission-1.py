from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. use dfs to explore neighbors
        # 2. initiate new components

        # 1. build adjacency
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        result = 0

        # 2. dfs to explore within the same component
        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # 3. find different component
        for node in range(n):
            if node not in visited:
                result += 1
                dfs(node)

        return result


