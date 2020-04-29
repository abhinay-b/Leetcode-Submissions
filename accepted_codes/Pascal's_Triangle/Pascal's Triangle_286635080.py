class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows == 0:
            return res
        res.append([1])
        if numRows == 1:
            return res
        for i in range(2,numRows+1):
            temp = [1]*i
            for j in range(len(res[-1])-1):
                temp[j+1] = res[-1][j] + res[-1][j+1]
            res.append(temp)
        return res
