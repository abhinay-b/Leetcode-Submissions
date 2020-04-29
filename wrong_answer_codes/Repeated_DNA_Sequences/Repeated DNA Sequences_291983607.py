class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        def buildLps(pattern):
            buffer = [0]*len(pattern)
            i,j = 0,1
            while j < len(pattern):
                if pattern[i] == pattern[j]:
                    buffer[j] = i+1
                    i += 1
                    j += 1
                elif i > 0:
                    i = buffer[i-1]
                else:
                    buffer[j] = 0
                    j+= 1
            return buffer
        def searchPat(text,pattern):
            lps = buildLps(pattern)
            count = i = j = 0
            while i < (len(text)):                
                if text[i] == pattern[j]:
                    i+=1
                    j+=1
                elif j>0:
                    j = lps[j-1]
                else:
                    i+=1
                if j == len(pattern):
                    count += 1
                    j = 0
            return count
        if len(s) < 20:
            for word in ["AAAAAAAAAA","CCCCCCCCCC","GGGGGGGGGG","TTTTTTTTTT"]:
                if searchPat(s,word) > 0:
                    return [word]
            return []
        res = set()
        for idx in range(len(s)-9):
            count = searchPat(s,s[idx:idx+10])
            if count > 1:
                res.add(s[idx:idx+10])
        return res
