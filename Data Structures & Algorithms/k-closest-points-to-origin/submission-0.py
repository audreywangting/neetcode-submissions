class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # get the distance to the origin first
        # store in heap as tuple (x, y)
        # put it into a list, add them into max heap
        # leave only k points in the max heap
        # heappush [0] is the k smallest

        heap = []
        for x, y in points:
            distance = x**2 + y**2 # sqrt not necessary 
            heapq.heappush(heap, (-distance, x, y)) 

            if len(heap) > k:
                heapq.heappop(heap)

            
        return [[x, y] for dist, x, y in heap]




