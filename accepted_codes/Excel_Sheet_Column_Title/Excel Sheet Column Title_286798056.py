class Solution:
    def convertToTitle(self, n: int) -> str:
        base = ord('A') - 1
        if n <= 0:
            return ""
        res = ""
        while n:
            rem = n % 26
            n = n // 26
            if rem == 0:
                rem = 26
                n -= 1
            res = chr(base+rem) + res
        return res
            
        
        
