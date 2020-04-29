class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def helper(dig1,dig2,start):
            if start == len(num):
                return True
            res = str(dig1+dig2)
            if res == num[start:start+len(res)]:
                helper(dig2,int(res),start+len(res))
            else:
                return False
        dig1 = dig2 = ""
        i = 0
        while i < len(num):
            dig1 += num[i]
            j = i+1
            while j < len(num):
                dig2 += num[j]
                if helper(int(dig1),int(dig2),j+1):
                    return True
                j += 1
            i += 1
        return False
