class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n < 0:
            return []
        if n == 0:
            return [0]
        def stringToDec(s):
            num = 0
            while s:
                num += int(s[0])*2**(len(s)-1)
                s = s[1:]
            return num
        res = ['0','1']
        for i in range(n-1):
            temp = []
            for word in res:
                temp.append('0'+word)
            for word in res[::-1]:
                temp.append('1'+word)
            res = temp
        return list(map(stringToDec,res))
