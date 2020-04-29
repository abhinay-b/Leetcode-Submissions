from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort(key=len,reverse=True)
        if s.isdigit():
            return True
        for word in wordDict:
            if word in s and self.wordBreak(s.replace(word,'1'),wordDict):
                return True
        return False

