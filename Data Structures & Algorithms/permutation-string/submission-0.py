class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check s1 in s2
        # s1 should be a substring in s2
        # sliding window? keep the window same as the s1
        # fixed size?

        # iterate thru s2, check the range of s1
        # if window word in s1 -> return True?
        left = 0
        for right in range(len(s2)): # 7
            if right >= len(s1): # > 3
                left += 1

            word = s2[left:right+1]
            if sorted(s1) == sorted(word):
                return True

        return False


