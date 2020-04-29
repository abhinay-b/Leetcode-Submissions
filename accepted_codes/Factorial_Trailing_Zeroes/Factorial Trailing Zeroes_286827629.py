class Solution:
    def trailingZeroes(self, n: int) -> int:
        total = 0  
        while n >= 5:
            n = n // 5
            total += n
        return total
