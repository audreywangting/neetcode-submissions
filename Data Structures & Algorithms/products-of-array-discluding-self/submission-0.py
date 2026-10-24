class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        """
        n = len(nums)
        ans = []
        for i in range(n):
            product = 1 # 每次都要重新歸1
            for j in range(n):
                if j != i:
                    product *= nums[j]
            ans.append(product)
        return ans
        """
        # prefix * suffix

        n = len(nums)

        # 1. build prefix
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # 2. build suffix
        suffix = [1] * n
        for i in range(n-2, -1, -1): # suffix[n-1] = 1, 最後一個數字已經初始化好了, 所以從n-2開始
            suffix[i] = suffix[i+1] * nums[i+1]

        # 3. build ans
        ans = [0] * n 
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]
        return ans