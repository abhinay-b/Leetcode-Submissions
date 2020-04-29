class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [matrix[i][0] for i in range(len(matrix))]
        
        res = []
        s_l,e_l = 0,len(matrix)-1
        s_b,e_b = 0,len(matrix[0])-1
        i,j = s_l,s_b
        lpos = bpos = 1
        while s_l <= e_l and s_b <= e_b:
            
            while s_b <= j <= e_b:
                res.append(matrix[i][j])
                j += bpos
            if s_b > j:
                e_l -= 1
                
            elif j > e_b:
                s_l += 1
            bpos *= -1
            i += lpos
            j += bpos
            
            while s_l <= i <= e_l:
                res.append(matrix[i][j])
                i += lpos
            if s_l > i:
                s_b += 1
            elif i > e_l:
                e_b -= 1
            lpos *= -1
            i += lpos
            j += bpos
        return res
