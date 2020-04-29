from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
                return 1
        if endWord not in wordList:
        visited = set()
        dictn = defaultdict(list)
        wordList = set(wordList)
            return 0
        for word in wordList:
            for i in range(len(word)):
                dictn[word[:i]+'$'+word[i+1:]].append(word)
        queue = deque()
        queue.append((beginWord,1))
        visited.add(beginWord)
        while queue:
            word,height = queue.popleft()
            for i in range(len(word)):
                for nhbr in dictn[word[:i]+'$'+word[i+1:]]:
                    if nhbr == endWord:
                        return height+1
                    if nhbr not in visited:
                        visited.add(nhbr)
                        queue.append((nhbr,height+1))
        return 0

