from collections import defaultdict,deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> 
        List[List[str]]:
        
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        visited = set()
        dictn = defaultdict(list)
        res = []
        for word in wordList:
            for i in range(len(word)):
                dictn[word[:i]+'$'+word[i+1:]].append(word)
        queue = deque()
        queue.append((beginWord,[beginWord],0))
        visited.add(beginWord)
        minVal = float('inf')
        while queue:
            word,ladder,count = queue.popleft()
            visited.add(word)
            for i in range(len(word)):
                for nhbr in dictn[word[:i]+'$'+word[i+1:]]:
                    if nhbr == endWord:
                        if count+1 < minVal:
                            res = [ladder+[endWord]]
                            minVal = count+1
                        elif count+1 == minVal:
                            res.append(ladder+[endWord])
                        continue
                    if nhbr not in visited and count < minVal:    
                        queue.append((nhbr,ladder+[nhbr],count+1))
        return res
