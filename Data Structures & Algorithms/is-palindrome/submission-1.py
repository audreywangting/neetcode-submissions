class Solution:
    def isPalindrome(self, s: str) -> bool:
        # step 1 - clean the string
        # step 2 - use two pointers, i from index 0, j from index len(s)-1, keep comparing
        s_cleaned = ''.join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(s_cleaned) -1

        while i < j:
            if s_cleaned[i] != s_cleaned[j]:
                return False
            i += 1
            j -= 1
            
        return True


