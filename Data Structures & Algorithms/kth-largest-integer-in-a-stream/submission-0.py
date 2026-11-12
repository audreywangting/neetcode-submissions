import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        minheap = []

        for num in self.nums:
            heapq.heappush(minheap, num)

            if len(minheap) > self.k:
                heapq.heappop(minheap)

        return minheap[0]