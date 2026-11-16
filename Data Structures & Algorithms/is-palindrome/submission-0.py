class Solution:
    def isPalindrome(self, s: str) -> bool:
        # step 1 - clean the string
        # step 2 - use two pointers, i from index 0, j from index len(s)-1, keep comparing
        s_cleaned = s.lowercase()
        s_cleaned = s_cleaned.strip()
