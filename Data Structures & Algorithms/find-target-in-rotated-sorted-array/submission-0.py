class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the sorted half, then use its bound to see if the target is in
        # if in, keep the half, if not, remove the half
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) //2

            if nums[mid] == target:
                return mid

            # left half is sorted
            elif nums[mid] > nums[right]:

                # target 在左半邊
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 # 已經比對 mid & right

                # target 在右半邊
                else:
                    left = mid + 1
            
            # right half is sorted
            else:
                # target 在右半邊
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # target 在左半邊
                else:
                    right = mid - 1

        return -1