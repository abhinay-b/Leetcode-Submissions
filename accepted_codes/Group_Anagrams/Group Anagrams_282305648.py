from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ctrList = defaultdict(list)
        for word in strs:
            alphabet = [0]*26
            for letter in word:
                alphabet[ord(letter) - ord('a')] += 1
            ctrList[tuple(alphabet)].append(word)                
        return ctrList.values()
        
