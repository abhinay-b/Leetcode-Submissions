class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == "":
            return path
        words = path.split("/")
        stack = []
        for word in words:
            if word == "" or word == ".":
                continue
            if word == "..":
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(word)
        res = ""
        if len(stack) == 0:
            return "/"
        for word in stack:
            res += "/" + word
        return res
