class Solution:
    def checkValidString(self, s: str) -> bool:
        left = right = star = 0
        visited = set()
        for idx,char in enumerate(s):
            if char == '(':
                left += 1
            elif char == ')':
                right += 1
                if right > left:
                    if star > 0:
                        star -= 1
                        left += 1
                        visited.add(idx)
                    else:
                        return False
            else:
                star += 1
        print(visited)
        left = right = star = 0
        for char in s[::-1]:
            if char == ')':
                right += 1
            elif char == '(':
                left += 1
                if left > right:
                    if star > 0:
                        star -= 1
                        right += 1
                    else:
                        return False
            elif idx not in visited:
                star += 1
        return True
