class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        """
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    if i != j:
                        return [i, j]
        """
        # hash map
        """
        seen = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] not in seen:
                seen[nums[i]] = i
            else:
                return [seen[target - nums[i]], i]
        """
        # better solution
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
                 
