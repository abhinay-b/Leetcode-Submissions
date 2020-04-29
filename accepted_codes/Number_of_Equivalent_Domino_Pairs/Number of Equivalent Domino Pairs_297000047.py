from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dictn = defaultdict(int)
        for pair in dominoes:
            dictn[min(pair)*10+max(pair)] += 1
        res = 0
        for value in dictn.values():
            res += value*(value-1) // 2 #nC2 = n*(n-1) / 2
        return res
