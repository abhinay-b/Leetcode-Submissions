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
        for idx,char in enumerate(s):
            #odd length palindrome
            count += countFromPos(idx,idx)
            #even length palindrome
            count += countFromPos(idx,idx+1)
        return count
