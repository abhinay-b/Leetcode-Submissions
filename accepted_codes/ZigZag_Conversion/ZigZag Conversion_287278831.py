class Solution:
    def convert(self, s: str, rows: int) -> str:
        if rows == 1 or len(s) == 0:
            return s
        substrLists = ["" for i in range(rows)]
        pos = 0
        step = -1
        for char in s:
            substrLists[pos] += char        
            if pos == 0 or pos == rows - 1:
                step *= -1
            pos += step
        result = ""
        return ''.join(substrLists)
