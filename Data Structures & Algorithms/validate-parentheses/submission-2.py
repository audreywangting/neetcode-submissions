class Solution:
    def isValid(self, s: str) -> bool:
        # when it's (, [, { => add to stack
        # create (), [], {} pair dict
        # when it's ), ], } => use the pair dict to pop the element in the stack
        # or return false
        # make sure the stack is not null before doing pop/push

        stack = []
        pair = {
            ')': '(',
            ']': '[', 
            '}': '{'
        }

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)

            elif stack and ch in pair and stack[-1] == pair[ch]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
