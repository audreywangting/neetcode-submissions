class Solution:

    def encode(self, strs: List[str]) -> str:
        # keep length & # as word's starting point
        encoded_string = ""
        for x in strs:
            n = len(x)
            encoded_string += str(n) + "#" + x

        return encoded_string

    def decode(self, s: str) -> List[str]:
        # use two pointer to get i(the word's len) & j(#'s position)
        # 5#Hello5#World

        i = 0
        decoded_strs = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j+1:length+j+1]
            decoded_strs.append(word)
            i = length + j + 1

        return decoded_strs




            
