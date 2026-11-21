class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use the mid to check if the list is rotated
        # the left half is not rotated: check if target is there
        # the right half is rotated: check if target is there
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid

            # left half is sorted
            elif nums[mid] >= nums[left]:
                # check target有沒有左邊裡面
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            
            else:
                # check target 有沒有在右邊裡面
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1


        
