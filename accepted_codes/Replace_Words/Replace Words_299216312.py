from collections import defaultdict
class Trie:
    def __init__(self):
        self.dictn = defaultdict(Trie)
        self.isEnd = False
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        available = defaultdict(str)
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
            if word not in available:                
                for idx,char in enumerate(word):
                    if char in temp.dictn:
                        temp = temp.dictn[char]
                        if temp.isEnd:
                            break
                    else:
                        break
                if temp.isEnd:
                    available[word] = word[:idx+1]
                else:
                    available[word] = word
            res += available[word] + " "
        return res[:-1]
        

