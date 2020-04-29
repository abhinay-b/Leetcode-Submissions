class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 11:
            return []        
        dictn = set()
        res = set()
        for idx in range(len(s)-9):
            pattern = s[idx:idx+10]
            if pattern in dictn:
                res.add(pattern)
            else:
                dictn.add(pattern)
        return res
