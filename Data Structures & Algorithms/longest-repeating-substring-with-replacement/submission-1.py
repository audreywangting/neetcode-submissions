class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # to maintain a sliding window containing the same ch
        # the window_len - max_cnt should <= k to make it longest
        left = 0
        max_len = 0
        count = {}
        max_freq = 0

        for right in range(len(s)):
            # expand the window
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(count[s[right]], max_freq)
                
            # when to shrink
            if (right-left+1) - max_freq > k:
                count[s[left]] -= 1
                left += 1 # 一定要先減, pointer才可以動

            max_len = max(right-left+1, max_len)

        return max_len

        