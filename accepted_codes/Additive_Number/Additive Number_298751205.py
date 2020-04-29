def is_additive_sequence(v1, v2, num):
    a, b = v1, v2
    
    i = 0
    while i < len(num):
        c = str(int(a) + int(b))
        if not num.startswith(c, i):
            return False
        i += len(c)
        a, b = b, c
    return True

def is_valid(num):
    return len(num) <= 1 or num[0] != '0'

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num)):
            for j in range(i+1, len(num)):
                v1, v2, rest = num[:i], num[i:j], num[j:]
                
                if not is_valid(v1) or not is_valid(v2):
                    continue
                                                                        
                if is_additive_sequence(v1, v2, rest):
                    return True
        return False
