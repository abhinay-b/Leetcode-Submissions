class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if not num:
            return True
        if len(num) < 3:
            return False
        def helper(dig1,dig2,start):
            # print(dig1,dig2,start)
            if start == len(num) and str(dig1)+str(dig2) == num:
                    return False
            while start < len(num):
                res = str(dig1+dig2)
                if res == num[start:start+len(res)]:
                    dig1,dig2,start = dig2,int(res),start+len(res)
                else:
                    return False
            return True
        dig1 = dig2 = ""
        i = 0
        while i < len(num):
            dig1 += num[i]
            j = i+1
            dig2 = ""
            while j < len(num):
                dig2 += num[j]
                if helper(int(dig1),int(dig2),j+1):
                    return True
                j += 1
                if dig2 == '0':
                    break
            if dig1 == '0':
                break
            i += 1            
            
        return False
