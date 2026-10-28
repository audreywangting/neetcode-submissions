class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window to maintain "longest substring w/o repeating chracters"
        # use set to record the appearance of the string
        # right pointer keep going right to expand the window
        # left pointer move to the right if the the character appeared in the set
        left = 0
        max_len = 0
        appeared = set() # 一開始要是空的，因為還沒開始看字串
        for right in range(len(s)):
            # 先持續檢查有沒有出現在字串中
            while s[right] in appeared:
                appeared.remove(s[left])
                left += 1
             
            appeared.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
                
            