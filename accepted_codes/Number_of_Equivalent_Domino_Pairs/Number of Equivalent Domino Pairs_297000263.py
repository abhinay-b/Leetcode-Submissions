from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = [0]*100
        for i, j in dominoes:
            if i > j:
                i, j = j, i
            dic[i*10+j] += 1 
        res = 0
        for i in range(11,100):
            if dic[i] > 1:
                res += (dic[i]-1)*dic[i]//2
        return res
