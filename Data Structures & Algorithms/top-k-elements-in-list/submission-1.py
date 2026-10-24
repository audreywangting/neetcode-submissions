from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use counter, then use sorted to get the top frequent elements
        count = Counter(nums)
        sort = sorted(count, key=lambda x: count[x], reverse=True)
        return sort[:k]