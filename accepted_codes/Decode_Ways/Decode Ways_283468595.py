class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == '0':
            return 0
        n = len(s)
        count = [0]*(n+1)
        count[0]=count[1] = 1
        for i in range(2,n+1):
            if int(s[i-1]) > 0:
                count[i] = count[i-1]
            if 9 < int(s[i-2:i]) < 27:
                count[i] += count[i-2]
        return count[n]
