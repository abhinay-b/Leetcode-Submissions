class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        sign = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        while(dividend >= divisor):
            count = 1
            temp = divisor
            while(dividend >= temp):
                temp <<= 1
                count <<= 1
            res += count >> 1
            dividend -= temp >> 1
        max = 2 ** 31 - 1
        
        if sign == True:
            res = -res
        if res > max:
            res = max

