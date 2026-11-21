class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
 # 前 3 分鐘： 不寫 code，先用英文解釋 approach。
# 接下來 12 到 17 分鐘： 自己實作，不看答案。
# 最後 3 到 5 分鐘： Dry run、確認 edge cases、分析 complexity。

        seen = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i