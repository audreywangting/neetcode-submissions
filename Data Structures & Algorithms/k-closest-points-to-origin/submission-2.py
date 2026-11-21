import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use maxheap with len not > k to maintain k closest points
        # use x**2 + y**2 as the distance

    
        maxheap = []
        for x, y in points:
            distance = (x**2 + y**2)
            heapq.heappush(maxheap, (-distance, x, y))

            if len(maxheap) > k:
                heapq.heappop(maxheap)

        return [[x, y] for _, x, y in maxheap]