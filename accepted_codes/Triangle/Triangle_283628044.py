class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        memo = triangle[-1]
        triangle = triangle[-2::-1]
        for ele in triangle:
            for j in range(len(ele)):
                memo[j] = ele[j] + min(memo[j],memo[j+1])
        return memo[0]
