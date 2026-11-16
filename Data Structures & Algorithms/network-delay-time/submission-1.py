from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # single source shortest path, weighted graph: use dijkstra 
        # use minheap: (time, node)
        # use adjacency graph to quickly get the node & dist (neighbor, time)
        # keep updating the time, when the len of visited == n, means we traversed all the nodes and we get the shortest path

        time = 0
        minheap = [(0, k)] # starting from k
        visited = set()
        graph = defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))

        # start dijkstra
        while minheap:
            time, node = heapq.heappop(minheap)

            if node in visited:
                continue

            visited.add(node)
            result = time

            # explore the neighbor

            for nei, weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(minheap, (time+weight, nei))

        return result if len(visited) == n else -1







