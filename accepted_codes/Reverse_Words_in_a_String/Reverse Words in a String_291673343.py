class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        s = list(s.split())
        return " ".join(s[::-1])
