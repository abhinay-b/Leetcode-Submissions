from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def distance(beginWord,endWord,d,visited):
            queue = deque()
            queue.append((beginWord,0))
            while queue:
                word,height = queue.popleft()
                for nhbr in d[word]:
                    if nhbr == endWord:
                        return height+1
                    if nhbr not in visited:
                        visited.add(nhbr)
                        queue.append((nhbr,height+1))
            return 0
        if endWord not in wordList:
            if beginWord == endWord:
                return 1
            return 0
        def diffBy1(word1,word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
                    if count > 1:
                        return False
            return True
        d = defaultdict(list)
        steps = 0
        for i in range(len(wordList)):
            for j in range(i+1,len(wordList)):
                if diffBy1(wordList[i],wordList[j]):
                    d[wordList[i]].append(wordList[j])
                    d[wordList[j]].append(wordList[i])
        if beginWord not in d:
            for i in range(len(wordList)):
                if diffBy1(wordList[i],beginWord):
                    beginWord = wordList[i]
                    steps += 1
                    break
        visited = set()
        path = distance(beginWord,endWord,d,visited)
        if path == 0:
            return path
        return steps+path

