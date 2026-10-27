class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use a for loop to fix one element, then use two pointers i & j to find the combinations
        # since i, j, k are distinct, need to prevent from duplications
        # return nums
        nums.sort()

        n = len(nums)
        ans = []
        for a in range(n):
            i = a+1 # make sure a < i < j, no duplications
            j = n-1

            # check if appeared and used
            if a > 0 and nums[a] == nums[a-1]: 
                continue

            while i < j:
                if nums[a] + nums[i] + nums[j] == 0:
                    ans.append([nums[a], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    # check if i == i+1 / j == j-1 
                    while i < j and nums[i] == nums[i-1]: # 是要跟上一個i比較
                    # 用 while 才能一直跳過！！
                        i += 1

                    while i < j and nums[j] == nums[j+1]:
                        j -= 1

                elif nums[a] + nums[i] + nums[j] > 0:
                    j -= 1

                else:
                    i += 1

                
        return ans


                    
