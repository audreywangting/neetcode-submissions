import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap, -stone)

        while len(maxheap) > 1:
            y = heapq.heappop(maxheap)
            x = heapq.heappop(maxheap)

            if y < x:
                y = y-x
                heapq.heappush(maxheap, y)

        return -maxheap[0] if len(maxheap) > 0 else 0 


        
