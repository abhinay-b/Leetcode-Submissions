class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if m == 0 and n == 0:
            return False
        if m == 1 and n == 1:
            return matrix[0][0] == target
        start,end = 0,m-1
        i = 0
        while start < end:
            mid = (start+end) // 2
            temp = matrix[mid][0]
            if temp == target:
                return True
            if temp > target:
                end = mid
            else:
                start = mid+1
        if start > 0:
            i = start-1
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
