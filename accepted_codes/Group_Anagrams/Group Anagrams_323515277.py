from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ctrList = defaultdict(list)
        for word in strs:
            ctrList["".join(sorted(list(word)))].append(word)                
        return ctrList.values()
        
