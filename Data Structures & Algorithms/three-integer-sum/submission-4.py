class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use for loop to fix one element + 2 pointers to check the combination
        # time complexity: O(n^2)
        result = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            left = i+1
            right = n-1
            # skip same i:
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # left & right should keep moving when duplicate
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif total > 0:
                    right -= 1

                else:
                    left += 1

                

        return result