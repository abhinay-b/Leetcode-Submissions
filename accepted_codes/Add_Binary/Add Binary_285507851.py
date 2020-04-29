class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i = j = 0
        a,b = a[::-1],b[::-1]
        carry = 0
        while i < len(a) and j < len(b):
            temp = int(a[i]) + int(b[j]) + carry
            carry = temp // 2
            temp %= 2 
            res += str(temp)
            i += 1
            j += 1
        while i < len(a):
            temp = int(a[i]) + carry
            carry = temp // 2
            temp %= 2 
            res += str(temp)
            i += 1
            if carry == 0:
                res += a[i:]
                break
        while j < len(b):
            temp = int(b[j]) + carry
            carry = temp // 2
            temp %= 2 
            res += str(temp)
            j += 1
            if carry == 0:
                res += b[j:]
                break
        if carry == 1:
            res += str(carry)
        return res[::-1]
