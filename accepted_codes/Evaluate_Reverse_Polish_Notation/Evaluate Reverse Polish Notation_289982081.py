class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return -1
        stack = []
        operators = {'+':lambda x,y : x+y,
                     '-':lambda x,y: x-y,
                    '*':lambda x,y: x*y,
                    '/':lambda x,y: int(x/y),}
        for char in tokens:
            if char not in operators:
                stack.append(char)
            else:
                if not stack:
                    return -1
                num1 = int(stack.pop())
                if not stack:
                    return -1
                num2 = int(stack.pop())
                stack.append(operators[char](num2,num1))
        return stack.pop()
