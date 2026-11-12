import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
        # 在 __init__ 建立 Heap，把 Heap 當成一個持續更新的資料結構
        self.minheap = []

        for num in self.nums:
            heapq.heappush(self.minheap, num) # O(logk)

            if len(self.minheap) > self.k:
                heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)

        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

        return self.minheap[0]