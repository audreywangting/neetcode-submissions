class Solution:
    def isValid(self, s: str) -> bool:
        # use dict to record the pairing (), [], {}
        # use stack to keep check the s
        # if ) and the top is ( then pop (
        # if ] and the top is [ then pop [
        # if } and the top is { then pop {
        stack = []
        pair = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        for ch in s:
            # 遇到左括號
            if ch in pair:
                stack.append(ch)

            # 遇到右括號
            else:
                if stack and ch == pair[stack[-1]]: #要先make sure stack不為空 不然stack[-1]會出錯
                    stack.pop()
                else:
                    return False
        return len(stack) == 0 # make sure stack是空的