from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictn = defaultdict(list)
        for word in wordDict:
            dictn[word[0]].append((word,len(word)))
        def search(start):
            if start >= len(s):
                return True
            for word in dictn[s[start]]:
                if word[0] == s[start:word[1]+start] and search(word[1]+start):
                    return True
            return False
        return search(0)
                
