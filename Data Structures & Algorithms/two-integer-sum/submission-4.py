class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force: O(n^2)
        """
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """
        
        # hashmap
        seen = {} # initialize dict
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]

            else:
                seen[nums[i]] = i