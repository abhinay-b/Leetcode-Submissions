from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 11:
            return []        
        res = defaultdict(int)
        for idx in range(len(s)-9):
            pattern = s[idx:idx+10]
            res[pattern] += 1
        return list(filter(lambda key: res[key]>1,res.keys()))
