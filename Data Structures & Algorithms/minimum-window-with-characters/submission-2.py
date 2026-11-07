class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. brute force: 
        # get all the substring
        # check if they have t
        # choose the shortest one

        # 2. use sliding window
        # expand when the sliding window doesn't include all t
        # shrink when all the t exists in s
        # use required & formed to quickly check the window
        # required: how many words need to be met
        # formed: how many words met the requirement now

        result = ""
        need = Counter(t) # t裡的ch個數
        have = {} # 現在window裡面的ch個數

        required = len(need) # 有幾種字元要達到要求
        formed = 0 # 目前有幾種字元達到要求

        min_len = float('inf')
        left = 0

        for right in range(len(s)): # expand
            ch = s[right]

            # expand
            have[ch] = have.get(ch, 0) + 1

            # 確認現在走到的這個ch，他這字元的要求是否滿足
            if ch in need and have[ch] == need[ch]:
                formed += 1

            # shrink
            while required == formed:
                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    result = s[left:right+1]

                # 開始移除最左的字元，
                left_ch = s[left]
                have[left_ch] -= 1

                # 要是不合規就要記錄
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
            
                left += 1
        return result




