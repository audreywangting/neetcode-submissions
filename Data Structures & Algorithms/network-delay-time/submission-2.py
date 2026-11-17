from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # single source, shortest path -> dijkstra
        # minheap + bfs
        # minheap : (time, node) starting from k
        # adjacency list to quickly find the time need

        minheap = [(0, k)]
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        visited = set()
        result = 0

        # 1. start minheap
        while minheap:
            time, node = heapq.heappop(minheap)

            # skip visited nodes
            if node in visited:
                continue

            # mark visited
            visited.add(node)
            result = time

            # explore neighbors
            for nei, wei in graph[node]:
                heapq.heappush(minheap, (time+wei, nei))

        return result if len(visited) == n else -1
