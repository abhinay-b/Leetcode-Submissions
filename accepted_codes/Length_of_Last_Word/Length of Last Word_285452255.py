class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "" or s == " ":
            return 0
        words = (s.strip()).split(" ")
        return len(words[-1])
