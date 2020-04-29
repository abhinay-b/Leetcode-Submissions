class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        n = len(triangle)
        count = []
        for entry in triangle:
            temp = []
            for ele in entry:
                temp.append(float('inf'))
            count.append(temp)
        print(count)
        count[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])-1):
                count[i][j] = min(count[i][j], triangle[i][j]+count[i-1][j])
                count[i][j+1] = min(count[i][j+1], triangle[i][j+1]+count[i-1][j])
            # print(count)
        return count[n-1][n-1]
