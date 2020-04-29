class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        for i,row in enumerate(matrix):
            for j,col in enumerate(row):
                if col == 0:
                    temp.append((i,j))
        if len(temp) == 0:
            return matrix
        for i in range(len(temp)):
            for j in range(len(matrix[temp[i][0]])):
                matrix[temp[i][0]][j] = 0
        for i in range(len(matrix)):
            for j in range(len(temp)):
                matrix[i][temp[j][1]] = 0
        return matrix
            
