class Solution:
    def isValid(self, s: str) -> bool:
        openPar = "({["
        closedPar = ")}]"
        balPar = "(){}[]"
        stack = []
        
        for char in s:
            if char in openPar:
                stack.append(char)
            elif char in closedPar:
                if len(stack) == 0:
                    return False
                temp = stack.pop() + char
                if temp not in balPar:
                    return False
        if len(stack) > 0:
            return False
        return True
