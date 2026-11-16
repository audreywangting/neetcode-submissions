from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # maintain a sliding window that contains t in s
        # use Counter to count t's ch 
        # keep min_len of the window and compare
        # if full t is not included in s then return ""


        result = "" 
        have = {} # ch in the window
        need = Counter(t) # ch in t
        min_len = inf

        for right in range(len(s)):
            have[s[right]] = have.get(s[right], 0) + 1
            min_len = min(min_len, right-left+1)


