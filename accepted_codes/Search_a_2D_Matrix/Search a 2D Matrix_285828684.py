class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0 or len(matrix[0]) == 0:
            return False
        n = len(matrix[0])        
        
        start,end = 0,m-1
        mid = (start+end) // 2
        i = 0
        while start < end:
            mid = (start+end) // 2
            temp = matrix[mid][0]
            if temp == target:
                return True
            if temp > target:
                end = mid
            elif target > matrix[mid][n-1]:
                start = mid+1
            else:
                i = mid
                break
        if matrix[i][0] == target:
            return True
        if start == end:
            i = end
        start,end = 0,n-1
        while start < end:
            mid = (start+end) // 2
            temp = matrix[i][mid]
            if temp == target:
                return True
            if temp > target:
                end = mid
            else:
                start = mid+1
        return matrix[i][start] == target
