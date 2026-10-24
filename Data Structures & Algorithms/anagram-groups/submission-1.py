class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use hashmap - dict to store words
        word = {}

        for x in strs:
            key = ''.join(sorted(x))
            # tuple(sorted(x))
            if key not in word:
                word[key] = []
            word[key].append(x)
        return list(word.values())