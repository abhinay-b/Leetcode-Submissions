class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return A
        left,right = 0,len(A)-1
        res = []
        while left <= right:
            leftSq = A[left]**2
            rightSq = A[right]**2
            if leftSq >= rightSq:
                res.append(leftSq)
                left+=1
            else:
                res.append(rightSq)
                right-=1
        return res[::-1]
