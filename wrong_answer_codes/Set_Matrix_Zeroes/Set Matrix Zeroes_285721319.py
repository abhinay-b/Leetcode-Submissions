class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = -1,-1
        for i,row in enumerate(matrix):
            for j,col in enumerate(row):
                if col == 0:
                    temp = i,j
                    break
        if temp[0] < 0:
            return matrix
        for j in range(len(matrix[temp[0]])):
            matrix[temp[0]][j] = 0
        for i in range(len(matrix)):
            matrix[i][temp[1]] = 0
        return matrix
            
