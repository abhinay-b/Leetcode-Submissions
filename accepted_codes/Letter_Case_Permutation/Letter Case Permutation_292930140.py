class Solution:
    def __init__(self):
            self.res = []
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return [""]
        S = S.lower()
        self.helper("",S)
        return self.res
    def helper(self,temp,word):
        if not word:
            self.res.append(temp)
            return
        self.helper(temp+word[0],word[1:])
        if ord('a') <= ord(word[0]) <= ord('z'):
            self.helper(temp+(word[0]).upper(),word[1:])
