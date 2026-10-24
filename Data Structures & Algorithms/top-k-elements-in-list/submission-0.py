from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use counter to record appear times and get top k?
        ans = []
        appear = Counter(nums)
        appear = sorted(appear, key= lambda x: appear[x], reverse=True) # sorted would return a list
        return appear[:k] # until top k
        