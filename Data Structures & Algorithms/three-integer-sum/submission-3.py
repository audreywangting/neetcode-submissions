class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use a for loop to fix one element, and two pointers i & j to explore combinations
        # when iterating the list, skip the duplicated element
        # if total == 0: add ans
        # if total < 0: i += 1
        # if total > 0: j -= 1
        # use ans [] to store element in the nums

        ans = []
        nums.sort()

        for x in range(len(nums)):
            i = x + 1
            j = len(nums) - 1

            # if x == x-1 to skip
            if x > 0 and nums[x] == nums[x-1]:
                continue

            # when found the triplet:
            while i < j:
                if nums[x] + nums[i] + nums[j] == 0:
                    ans.append([nums[x], nums[i], nums[j]])
                    i += 1
                    j -= 1

                    # update i
                    while i < j and nums[i] == nums[i-1]:
                        i += 1

                    while i < j and nums[j] == nums[j+1]:
                        j -= 1

                elif nums[x] + nums[i] + nums[j] < 0:
                    i += 1

                else:
                    j -= 1
                    

        return ans

            
            
