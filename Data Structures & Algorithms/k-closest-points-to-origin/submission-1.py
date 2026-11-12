import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use maxheap to store the points and its distance to the origin
        # iterate the points, and then push them the maxheap 
        # if maxheap len > k, the element in the maxheap are the k closest points to the origin

        maxheap = []

        for x, y in points:
            dist = x**2 + y**2

            heapq.heappush(maxheap, (-dist, x, y))

            if len(maxheap) > k:
                heapq.heappop(maxheap)


        return [[x, y] for dist, x, y in maxheap]
