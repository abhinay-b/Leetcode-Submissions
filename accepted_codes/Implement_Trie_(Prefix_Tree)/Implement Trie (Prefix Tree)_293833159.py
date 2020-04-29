class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None]*26
        self.isEnd = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self
        for char in word:
            idx = ord(char)-ord('a')
            if not temp.children[idx]:
                temp.children[idx] = Trie()
            temp = temp.children[idx]
        temp.isEnd = True
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self
        for char in word:
            idx = ord(char)-ord('a')
            if not temp.children[idx]:
                return False
            temp = temp.children[idx]
        return temp.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self
        for char in prefix:
            idx = ord(char)-ord('a')
            if not temp.children[idx]:
                return False
            temp = temp.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
