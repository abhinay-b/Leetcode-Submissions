class Solution:
    def mySqrt(self, x: int) -> int:
        start,end = 0,x
        if x < 2:
            return x
        while(start < end):
            mid = (start+end) // 2
            if mid == start:
                return mid
            if mid**2 > x:
                end = mid
            elif mid**2 < x:
                start = mid
            else:
                return mid
            
        return start
            
