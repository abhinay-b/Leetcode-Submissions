class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        n1 = n2 = 0
        for index,digit in enumerate(num1,1):
            n1 *= 10
            n1 += (ord(digit) - ord('0'))
        for index,digit in enumerate(num2,1):
            n2 *= 10
            n2 += (ord(digit) - ord('0'))
        res = n1 * n2
        result = ''
        while res > 0:
            result = str(res%10) + result
            res //= 10
        return result
