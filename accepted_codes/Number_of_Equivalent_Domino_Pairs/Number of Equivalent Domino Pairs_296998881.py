from math import factorial
class Solution:
    def combinations(self,number, taken):
        if number <= 0:
            return 0
        return factorial(number) // (factorial(taken) * factorial(number-taken))
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        if not dominoes or not dominoes[0]:
            return 0
        for i,x in enumerate(dominoes):
            dominoes[i][0],dominoes[i][1] = min(x[0],x[1]),max(x[0],x[1])
        dominoes.sort()
        count = res = 0
        i = 0
        while i < len(dominoes):
            count = 0
            while i < len(dominoes)-1 and ((dominoes[i][0] == dominoes[i+1][0] and 
                dominoes[i][1] == dominoes[i+1][1]) or (dominoes[i][0] == dominoes[i+1][1] and 
                dominoes[i][1] == dominoes[i+1][0])):
                count += 1
                i += 1
            if count:
                res += self.combinations(count+1,2)
            i += 1
        return res
