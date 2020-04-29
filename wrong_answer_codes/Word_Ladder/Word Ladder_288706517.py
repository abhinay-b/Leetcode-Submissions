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
                    mindist = min(mindist,temp)
            return mindist
        if endWord not in wordList:
            if beginWord == endWord:
                return 1
            return 0
        c = [{char:idx for idx,char in enumerate(word)} for word in wordList]
        d = defaultdict(list)
        steps = 1
        for i in range(len(c)):
            word1 = ''.join(c[i].keys())
            for j in range(i+1,len(c)):
                if len(c[i].items() - c[j].items()) == 1:
                    word2 = ''.join(c[j])
                    d[word1].append(word2)
                    d[word2].append(word1)
        if beginWord not in d:
            count = {char:idx for idx,char in enumerate(beginWord)}
            for i in range(len(c)):
                if len(c[i].items() - count.items())== 1:
                    beginWord = ''.join(c[i])
                    steps += 1
                    break
        visited = set()
        steps += distance(beginWord,endWord,d,visited)
        if steps < float('inf'):
            return steps
        return 0
