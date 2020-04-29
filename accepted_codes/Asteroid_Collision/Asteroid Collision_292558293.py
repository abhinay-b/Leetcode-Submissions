class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) < 2:
            return asteroids
        stack,res = [],[]
        for ast in asteroids:
            if ast >= 0:
                stack.append(ast)
            else:
                while stack and stack[-1] < abs(ast):
                    stack.pop()
                if not stack:
                    res.append(ast)
                elif stack[-1] == abs(ast):
                    stack.pop()
        return res+stack
