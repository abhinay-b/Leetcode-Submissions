from collections import defaultdict
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        dictn = defaultdict(str)
        available = set()
        for word in dict:
            available.add(word)
        words = sentence.split(" ")
        for word in words:
            temp = ""
            dictn[word] = word
            for char in word:
                temp += char
                if temp in available:
                    dictn[word] = temp
                    break
        res = ""
        for word in words:
            res += dictn[word] + " "
        return res[:-1]

