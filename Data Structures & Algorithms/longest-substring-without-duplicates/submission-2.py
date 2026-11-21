# use sliding window to find out the longest subtring
# use the right pointer to keep expanding, and the left pointer to shrink when there is duplicated elements in the window
# maintain a set to know if the new element is duplicated 
# keep comparing the max_len of the subtring to return the longest one

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        max_len = 0 # if theres no word
        seen = set()
        for right in range(n):
            # 1. if duplicated
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])

            max_len = max(max_len, right - left +1)

        return max_len




