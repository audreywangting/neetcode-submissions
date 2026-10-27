class Solution:
    def isPalindrome(self, s: str) -> bool:
        # step 1: clean the string
        # step 2: use tow pointers to compare the left & right hand side of element
            #  return traue if they're same, else: false

        s_cleaned = ''.join(c for c in s if c.isalnum()).lower()
        
        i = 0
        j = len(s_cleaned) - 1
        while i < j:
            if s_cleaned[i] != s_cleaned[j]:
                return False
            i += 1
            j -= 1

        return True
        