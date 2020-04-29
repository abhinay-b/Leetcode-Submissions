class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        while s:
            res += (ord(s[0])-ord('A')+1)*26**(len(s)-1)
            s = s[1:]
        return res
