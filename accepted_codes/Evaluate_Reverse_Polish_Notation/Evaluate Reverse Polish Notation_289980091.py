class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return -1
        stack = []
        operators = '+-*/'
        for char in tokens:
            if char not in operators:
                stack.append(char)
            else:
                if stack:
                    num1 = int(stack.pop())
                else:
                    return -1
                if stack:
                    num2 = int(stack.pop())
                else:
                    return -1
                if char == '+':
                    num2 += num1
                elif char == '-':
                    num2 -= num1
                elif char == '*':
                    num2 *= num1
                else:
                    num2 /= num1
                    num2 = int(num2)
                stack.append(num2)
        return stack.pop()
