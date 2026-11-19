class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # use greedy: at each step, see how far can you go
        max_reach = 0
        
        for i in range(len(nums)):
            if i > max_reach:
                return False # 永遠到不了

            max_reach = max(max_reach, i + nums[i])

        return True
