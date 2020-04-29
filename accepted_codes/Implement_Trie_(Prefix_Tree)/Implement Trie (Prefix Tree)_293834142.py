from collections import defaultdict
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = defaultdict(Trie)
        self.isEnd = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self
        for char in word:
            if char not in temp.children:
                temp.children[char] = Trie()
            temp = temp.children[char]
        temp.isEnd = True
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self
        for char in word:
            if char not in temp.children:
                return False
            temp = temp.children[char]
        return temp.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self
        for char in prefix:
            if char not in temp.children:
                return False
            temp = temp.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
