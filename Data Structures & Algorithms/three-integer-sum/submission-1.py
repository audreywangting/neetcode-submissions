class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # step 1 - sort the nums
        # step 2 - fix one element w/ loop, then use i & j
        # [-4, -1, -1, 0, 1, 2]
        # !! skip the duplicate elements

        nums.sort()
        ans = []
        for a, x in enumerate(nums):
            i = a + 1
            j = len(nums)-1
            if a > 0 and nums[a] == nums[a-1]: # 檢查目前的數字是否已經被前一次迴圈處理過
                continue

            while i < j:
                target = x + nums[i] + nums[j]
                if target < 0:
                    i += 1
                elif target > 0:
                    j -= 1
                else:
                    ans.append([x, nums[i], nums[j]])
                    i += 1
                    j -= 1

                    # 跳過左邊重複的元素
                    while i < j and nums[i] == nums[i-1]:
                        i += 1

                    # 跳過右邊重複的元素
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                    

        return ans



            
