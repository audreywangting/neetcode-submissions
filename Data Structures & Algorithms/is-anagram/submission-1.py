from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use hashmap to record appear times
        # use counter() ?
        return True if Counter(s) == Counter(t) else False