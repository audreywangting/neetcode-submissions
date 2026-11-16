import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # single source shortest path w/ no negative weight -> dijkestra
        # build adjacency list to quickly know the dist between nodes
        # use minheap to choose the node w/ shortest path
        # minheap saves: (distance, node)
        # after popping the node, explore its neighbors

        # 1. build adjacency list
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        # graph = {2:[3, 1], 3:[4, 1]}
        
        # 2. initialize min heap
        minheap = [(0, k)] # starting from k
        visited = set()
        result = 0

        # 3. start Dijkstra
        while minheap:
            time, node = heapq.heappop(minheap)

            # skip visited nodes 
            if node in visited:
                continue

            # mark visited 
            visited.add(node)
            result = time

            # explore neighbors
            for nei, weight in graph[node]:
                heapq.heappush(minheap, (time+weight, nei))

        return result if len(visited) == n else -1







