class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use binary search
        # left = 0, right = len(nums)-1, mid=(left+right)//2
        # check if rotated by comparing nums[mid] vs. nums[right]
        # if nums[mid] == target: return mid
        # use bound see if target is in the left or right, drop the half
        # if rotated: eg. 3,4,5,6,1,2
            # if in the left: nums[left] <= target < nums[mid]
                # drop right
            # else: in the right
                # drop left
        # if not rotated: eg. 1, 2, 3, 4, 5, 6
            # if in the right: nums[mid] < target <= nums[right]
                # drop left
            # else: in the left
                # drop right

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) //2

            if nums[mid] == target:
                return mid

            # 1. rotated:
            elif nums[mid] > nums[right]:
                # check the sorted part: left
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid +1

            # 2. not rotated:
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1

        return -1

            




