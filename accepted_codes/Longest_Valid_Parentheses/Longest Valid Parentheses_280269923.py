class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        left = right = 0
        res = 0
        for char in s:
            if char == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, left+right)
            elif left < right:
                left = right = 0
        left = right = 0
        for char in s[::-1]:
            if char == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, left+right)
            elif left > right:
                left = right = 0
        return res
        
                
