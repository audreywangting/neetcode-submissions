import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use minheap to keep the largest kth
        # k elements in the heap
        # the smallest in the heap is the kth largest in the array

        heap = []

        for nums in nums:
            heapq.heappush(heap, nums) # module, then list

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]