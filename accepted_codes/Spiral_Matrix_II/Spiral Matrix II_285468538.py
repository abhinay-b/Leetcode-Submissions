class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        l_start, l_end = 0,n-1
        b_start, b_end = 0,n-1
        lpos = bpos = num = 1
        i = j = 0
        while num <= (n**2):
            while b_start <= j <= b_end:
                mat[i][j] = num
                num += 1
                j += bpos
            bpos *= -1
            if j > b_end:
                j = b_end
                l_start += 1
            elif j < b_start:
                j = b_start
                l_end -= 1
            i += lpos
            while l_start <= i <= l_end:
                mat[i][j] = num
                num += 1
                i += lpos
            lpos *= -1
            if i > l_end:
                i = l_end
                b_end -= 1
            elif i < l_start:
                i = l_start
                b_start += 1
            j += bpos
        return mat
            
