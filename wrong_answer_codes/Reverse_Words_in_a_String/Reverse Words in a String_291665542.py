class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        s = s.strip()
        return ' '.join(s.split(" ")[::-1])
