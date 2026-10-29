from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 用 sliding window 找到所有有包含全部 t 的字元的 window, 再盡可能縮小，並記錄最短的 valid window
        # expand: 不停往右邊 expand
        # shrink: 只要目前window已包含所有t的字元，就嘗試縮小
        # update: 每次縮小前，檢查是否有更短的valid window


        result = "" 
        have = {} # ch in the window
        need = Counter(t) # ch in t

        required = len(need) # 有多少種字元需要達到要求，計算 dictionary 裡有幾個不同的 key
        formed = 0 # 計算有幾種字元已達需求

        min_len = float('inf')
        left = 0

        for right in range(len(s)):
            ch = s[right]
            
            # expand
            have[ch] = have.get(ch, 0) + 1

            # check if this chracter's requirement is fulfilled
            if ch in need and have[ch] == need[ch]:
                formed += 1 # 已經有個 ch 滿足要求！
            
            # shrink when window is valid
            while required == formed:
                window_len = right-left+1
                
                if window_len < min_len:
                    min_len = window_len
                    result = s[left:right+1]

                have[s[left]] -= 1
                # check if the window becoms invalid
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1
                

        return result


