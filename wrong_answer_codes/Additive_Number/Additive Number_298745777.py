class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if not num:
            return True
        if len(num) < 3:
            return False
        def helper(dig1,dig2,start):
            if start == len(num):
                if str(dig1)+str(dig2) == num:
                    return False
                return True
            res = str(dig1+dig2)
            if res == num[start:start+len(res)]:
                return helper(dig2,int(res),start+len(res))
            else:
                return False
        dig1 = dig2 = ""
        i = 0
        if int(num) == 0:
            return True
        if num[0] == '0':
            return False
        while i < len(num):
            dig1 += num[i]
            i += 1            
            j = i
            dig2 = ""
            while j < len(num):
                dig2 += num[j]
                if num[j] == '0':
                    if helper(int(dig1),int(dig2),j+1):
                        return True
                    else:
                        break
                j += 1
                if helper(int(dig1),int(dig2),j):
                    return True
        return False
