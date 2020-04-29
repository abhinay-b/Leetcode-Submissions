class Solution:
    def isValid(self, s: str) -> bool:
        openPar = "({["
        closedPar = ")}]"
        balPar = "(){}[]"
        stack = []
        if s == "":
            return s
        for char in s:
            if char in openPar:
                stack.append(char)
            elif char in closedPar:
                temp = stack.pop() + char
                if temp not in balPar:
                    return False
        return True
