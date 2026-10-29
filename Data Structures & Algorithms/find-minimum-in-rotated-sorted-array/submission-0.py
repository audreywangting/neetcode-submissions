class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use binary search to find the min
        # mid = left + right // 2
        # compare nums[mid] vs. nums[right] to see where is the smallest num
        # if nums[mid] > nums[right]: rotated -> in right
        # if nums[mid] <= nums[right]: min = nums[mid] or in the left

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) //2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]