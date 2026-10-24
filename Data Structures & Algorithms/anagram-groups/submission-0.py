# from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use dictionaruy to store word info
        # dict: {"act": "act", "cat"}
        word_dict = {}

        for x in strs:
            key = tuple(sorted(x)) # sorted(x) would return list!!! eg. sorted("act") = 'a', 'c', 't'
            # or can use: ''.join(sorted(x))

            if key not in word_dict:
                word_dict[key] = []
            
            word_dict[key].append(x)

        return list(word_dict.values())
            


