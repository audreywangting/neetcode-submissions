import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use min heap to keep size k of list to record the kth largest number
        # iterate the nums, push each element into minheap
        # if the len of minheap > k, then pop smallest element
        # minheap[0] = kth largest element

        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)


        return heap[0]
        