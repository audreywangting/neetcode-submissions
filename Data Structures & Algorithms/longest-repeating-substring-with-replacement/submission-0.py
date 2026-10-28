class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # key: 先思考花費成本，再實際操作
        # 重點：window每次維護的是目前valid的窗口
        # 用 max_freq 去維護現在window中出現最多次的element
        # window_length 確保我現在要改元素的window是可以return 最長的
        # 用 window_length - max_freq 知道目前 window 裡，最少需要替換幾個字元

        max_freq = 0
        max_len = 0
        count = {}
        left = 0

        for right in range(len(s)):
            # 1. expand the window
            char = s[right]
            count[char] = count.get(char, 0) + 1 # 如果這個字元出現過就+1, 沒出現過就從0開始+1

            # 2. update the max_freq
            max_freq = max(max_freq, count[char])

            # 3. shrink if there are too many adjustments needed 
            while (right-left+1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # 4. update the longest length
            max_len = max(max_len, right-left+1)
        return max_len



                