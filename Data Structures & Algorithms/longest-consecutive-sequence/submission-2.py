class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use set to store the element
        # check if k-1 in the set, if not then initialize length 
        # maintain max_len to keep compare different combination
        
        element = set(nums)
        max_len = 0

        for num in element:
            if num - 1 not in element:
                length = 1
                current = num
                while current + 1 in element:
                    length += 1
                    current += 1

                max_len = max(max_len, length)

        return max_len