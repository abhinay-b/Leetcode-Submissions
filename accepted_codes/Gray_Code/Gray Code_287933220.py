class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n < 0:
            return []
        if n == 0:
            return [0]
        res = [0]
        highestBit = 1
        for _ in range(n):
            res += [highestBit+num for num in res[::-1]]
            highestBit <<= 1
        return res
