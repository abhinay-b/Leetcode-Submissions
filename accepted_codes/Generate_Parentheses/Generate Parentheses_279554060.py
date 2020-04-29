class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def paranth(res,n,m):
            if n == m == 0:
                result.append(res)
            else:
                if n > 0:
                    paranth(res+'(',n-1,m)
                if m > n:
                    paranth(res+')',n,m-1)
        paranth("",n,n)
        return result
