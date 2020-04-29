class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int1 = int2 = 0
        len1,len2 = len(num1), len(num2)
        for idx,digit in enumerate(num1,1):
            digit = int(digit)
            int1 += digit*10**(len1-idx)
        for idx,digit in enumerate(num2,1):
            digit = int(digit)
            int2 += digit*10**(len2-idx)
        return str(int1*int2)
