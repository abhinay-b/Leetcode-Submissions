class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0 or len(matrix[0]) == 0:
            return False
        n = len(matrix[0])        
        
        start,end = 0,m*n-1
        mid = (start+end) // 2
        while start <= end:
            mid = (start+end) // 2
            temp = matrix[mid//n][mid%n]
            if temp == target:
                return True
            if temp > target:
                end = mid - 1
            else:
                start = mid+1
            
        return False
