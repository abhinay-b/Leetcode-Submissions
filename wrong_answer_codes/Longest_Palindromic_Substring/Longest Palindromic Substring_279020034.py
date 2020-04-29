class Solution:
    def expand(self, s:str, begin:int, end:int) -> str:
        while(begin >= 0 and end < len(s) and s[begin] == s[end]):
            begin -= 1
            end += 1
        return s[begin+1:end]
    def longestPalindrome(self, s: str) -> str:
        s = s.strip()
        maxStr = ""
        for index,char in enumerate(s):
            sub1 = self.expand(s,index,index)
            sub2 = self.expand(s,index,index+1)
            if len(maxStr) < len(sub1):
                maxStr = sub1
            elif len(maxStr) < len(sub2):
                maxStr = sub2
        if len(maxStr) <= 1:
                maxStr = ""
            # maxStr = max(sub1,sub2,maxStr)
        return maxStr
