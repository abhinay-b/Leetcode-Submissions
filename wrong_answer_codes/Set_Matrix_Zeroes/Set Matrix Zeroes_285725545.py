class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if not matrix:
            return matrix
        firstCol = False
        if matrix[0][0] == 0:
            firstCol = True
        for i,row in enumerate(matrix):
            for j,col in enumerate(row):
                if col == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(1,len(matrix[0])):
                matrix[0][j] = 0
        if firstCol:
            for i in range(1,len(matrix)):
                matrix[i][0] = 0
        return matrix
            
