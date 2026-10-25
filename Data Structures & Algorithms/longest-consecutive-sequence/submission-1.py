class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use set for quick existence check
        nums_set = set(nums)
        longest = 0
        for x in nums:
            if x - 1 not in nums_set:
                length = 1

                # 只有找到起點的時候才開始計算
                while x + length in nums_set: 
                    # 因為是while, 只有length不同增加，所以直接用+length
                    length += 1


                longest = max(length, longest)

        return longest
