from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictn = defaultdict(list)
        for word in wordDict:
            dictn[word[0]].append(len(word))
        def search(start):
            if start >= len(s):
                return True
            for word in dictn[s[start]]:
                if search(word+start):
                    return True
            return False
        return search(0)
                
