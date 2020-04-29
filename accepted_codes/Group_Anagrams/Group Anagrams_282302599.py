from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ctrList = list()
        wordList = list()
        for word in strs:
            ctr = Counter(word)
            if ctr in ctrList:
                idx = ctrList.index(ctr)
                wordList[idx].append(word)
            else:
                ctrList.append(ctr)
                wordList.append([word])
                
        return wordList
        
