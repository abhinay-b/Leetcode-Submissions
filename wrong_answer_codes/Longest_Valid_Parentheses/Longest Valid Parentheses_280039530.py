class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = []
        if len(s) < 2:
            return res
        for char in s:
            if char == "(":
                stack.append(char)
            elif len(stack) > 0:
                stack.pop()
                res += 2
        return res
