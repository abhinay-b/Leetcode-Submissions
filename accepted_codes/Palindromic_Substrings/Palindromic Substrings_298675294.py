class Solution:
    def countSubstrings(self, s: str) -> int:
        def countFromPos(pos1,pos2):
            count = 0
            while pos1 >= 0 and pos2 < len(s) and s[pos1] == s[pos2]:
                count += 1
                pos1 -= 1
                pos2 += 1
            return count
        count = 0
        if len(s) <= 1:
            return len(s)
        left = right = 0
        while left < len(s):
            while right < len(s) and s[left] == s[right]:
                right += 1
            temp = right - left
            count += temp*(temp+1) // 2
            count += countFromPos(left-1,right)
            left = right
            
        return count
