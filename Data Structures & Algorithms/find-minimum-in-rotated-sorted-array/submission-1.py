class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use binary search
        # set left = 0, right = len(nums) - 1, mid = (left+right)//2
        # compare nums[mid] vs. nums[right]
        # if >: rotated, min is in right, drop left half
        # else: not rotated, min is in the left, drop right half

        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left+right) //2
            if nums[mid] > nums[right]:
                left = mid +1
            else:
                right = mid # 因為是else, nums[mid] <= nums[right], -1會直接排除掉mid

        return nums[left]


