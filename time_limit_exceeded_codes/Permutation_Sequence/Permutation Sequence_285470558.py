class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        s = ""
        for i in range(1,n+1):
            s += str(i)
        def buildAll(add,string):
            if string == "":
                res.append(add)
                return
            for idx,char in enumerate(string):
                buildAll(add+char,string[:idx]+string[idx+1:])
        buildAll("",s)
        res.sort()
        if k <= len(res):
            return res[k-1]
        return ""
