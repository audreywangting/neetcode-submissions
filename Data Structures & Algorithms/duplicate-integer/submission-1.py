class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force: O(n2) -> TLE
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
                
        return False
        """
        # hash to keep what num has appeared
        appeared = {}
        for i, x in enumerate(nums):
            if x not in appeared:
                appeared[x] = i
            else:
                return True
        return False