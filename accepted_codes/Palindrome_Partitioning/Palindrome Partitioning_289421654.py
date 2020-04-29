class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        if len(s) == 1:
            return [s]
        def isPalindrome(start,end):
            combo = []
            count = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                t = s[start]
                if combo:
                    t += combo[-1][0]
                if end-start:
                    t += s[end]
                count = (end-start)+1
                combo.append((t,count))
                allPals[start].append((t,count))
                start -= 1
                end += 1
            return combo
        def grow(temp,start):
            if start >= len(s):
                res.append(temp) 
                return
            for combo in allPals[start]:
                grow(temp+[combo[0]],start+combo[1])
        allPals = [[] for _ in range(len(s))]
        for i in range(len(s)):
            isPalindrome(i,i)
            if i < len(s)-1:
                isPalindrome(i,i+1)
        res = []
        grow([],0)
        return res
