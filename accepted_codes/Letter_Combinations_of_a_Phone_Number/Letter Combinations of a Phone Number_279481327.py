class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        output = []
        def growLetters(res, digits):
            if len(digits) == 0:
                output.append(res)
            else:
                for ltr in phone[digits[0]]:
                    growLetters(res+ltr,digits[1:])
        if digits:
            growLetters("",digits)
        return output
