class Solution:
    def reverseBits(self, n: int) -> int:
        rev = bin(n)[:1:-1]
        rev += '0'*(32-len(rev))
        return int(rev,2)
