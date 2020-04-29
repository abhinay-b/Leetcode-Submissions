class Solution:
    def longestValidParentheses(self, s: str) -> int:
        curr = 0
        res = 0
        stack = [-1]
        if len(s) < 2:
            return -1
        for idx,char in enumerate(s):
            if char == "(":
                stack.append(idx)
            else:
                temp = stack.pop()
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    curr = idx - stack[-1]
                    res = max(curr,res)
        return res
