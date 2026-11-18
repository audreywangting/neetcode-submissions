import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # single source shortest path  -> dijkestra: bfs + minheap
        # minheap: (time, node)
        # graph: node: next, time
        # q: node to be counted?

        graph = defaultdict(list)
        result = 0
        minheap = [(0, k)] # starting from k
        visited = set()

        # 1. build adjacency list
        for u, v, w in times:
            graph[u].append((v, w))

        # 2. start bfs
        while minheap:
            time, node = heapq.heappop(minheap)

            if node in visited:
                continue

            visited.add(node)

            result = time
            for nei, wei in graph[node]:
                heapq.heappush(minheap, (time+wei, nei))

        return result if len(visited) == n else -1
            
        

