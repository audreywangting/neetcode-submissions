class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use hashmap - dict to store words
        """
        word = {}

        for x in strs:
            key = ''.join(sorted(x))
            # tuple(sorted(x))
            if key not in word:
                word[key] = []
            word[key].append(x)
        return list(word.values())
        """
        # use counter() -> improve time complexity to O(n*k)
        # just change the way of keeping key (from sorted to counter)
        word = {}
        for x in strs:
            count = [0] * 26
            for c in x:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in word:
                word[key] = []
            word[key].append(x)
        return list(word.values())



