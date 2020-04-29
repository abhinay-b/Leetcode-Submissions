from collections import defaultdict
class Trie:
    def __init__(self):
        self.dictn = defaultdict(Trie)
        self.isEnd = False
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        dictn = defaultdict(str)
        trie = Trie()
        temp = trie
        for word in dict:
            temp = trie
            for char in word:
                if char not in temp.dictn:
                    temp.dictn[char] = Trie()
                temp = temp.dictn[char]
            temp.isEnd = True
                
        words = sentence.split(" ")
        res = ""
        for word in words:
            temp = trie
            for idx,char in enumerate(word):
                if char in temp.dictn:
                    if temp.isEnd:
                        break
                    temp = temp.dictn[char]
                else:
                    break
            if temp.isEnd:
                res += word[:idx]
            else:
                res += word
            res += " "
        return res[:-1]
        res = ""
        for word in words:
            res += dictn[word] + " "
        return res[:-1]

