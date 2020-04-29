from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def distance(beginWord,endWord,d,visited):
            if beginWord == endWord:
                return 0
            mindist = float('inf')
            visited.add(beginWord)
            for nhbr in d[beginWord]:
                if nhbr not in visited:
                    temp = 1+distance(nhbr,endWord,d,visited)
                    visited.discard(nhbr)
                    mindist = min(mindist,temp)
            return mindist
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
        steps = 1
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
        steps += distance(beginWord,endWord,d,visited)
        if steps < float('inf'):
            return steps
        return 0
