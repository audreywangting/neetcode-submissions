class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use prefix & suffix to get O(n)
        
        n = len(nums)

        # 1. prefix's product
        # [1, 1, 2, 8]
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        # 2. suffix's product
        # [48, 24, 6, 1]
        suffix = [1] * n
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        # 3. ans
        ans = [1] * n
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]

        return ans


