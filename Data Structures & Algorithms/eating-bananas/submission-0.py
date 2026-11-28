class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # banana per hr: k
        # use binary search to find 在 [1, max(piles)] 裡最小的 feasible speed
        # k 小                            k 大
        # ↓                               ↓
        # False False False | True True True
        #                   ↑
        #                 找這個
        left = 1
        right = max(piles)
        while left < right:
            mid = (left+right) // 2
            hours = 0
            for pile in piles:
                hours += (pile + (mid - 1))//mid # 無條件進位

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left
            