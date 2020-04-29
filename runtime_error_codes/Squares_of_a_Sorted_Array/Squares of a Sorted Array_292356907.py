class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return A
        left,right = 0,len(A)-1
        res = []
        leftSq,rightSq = A[left]**2, A[right]**2
        while left <= right:            
            if leftSq >= rightSq:
                res.append(leftSq)                
                left+=1
                leftSq = A[left]**2
            else:
                res.append(rightSq)
                right-=1
                rightSq = A[right]**2
        return res[::-1]
