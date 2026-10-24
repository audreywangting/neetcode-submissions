class Solution:

    # point: how to reverse the string
    # eg. "Hello", "World"
    # why not return "Hello World" >> use length + # to seperate the word
    # eg. 5#Hello5#World
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for x in strs:
            n = len(x)
            x_encoded = str(n) + '#' + x
            encoded_string += x_encoded
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # use two pointer to find the word
        i = 0 # the number's start point
        # j to find #, +1 would be the word's start
        decoded_strs = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 # keep searching 

            length = int(s[i:j])
            decoded_strs.append(s[j+1:length+j+1])
            i = length+j+1

        return decoded_strs
