class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def helper(temp,word):
            if not word:
                res.append(temp)
                return
            helper(temp+word[0],word[1:])
            if ord('a') <= ord(word[0]) <= ord('z'):
                helper(temp+(word[0]).upper(),word[1:])
        if not S:
            return [""]
        S = S.lower()
        res = []
        helper("",S)
        return res
