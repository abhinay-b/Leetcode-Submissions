from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ctrList = defaultdict(list)
        for word in strs:
            ctr = Counter(word)
            ctrList["".join(sorted(ctr))].append(word)                
        return ctrList.values()
        
