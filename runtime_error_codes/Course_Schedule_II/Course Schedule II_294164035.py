from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def Helper(idx):
            if idx in visited:
                return True
            if idx in inStack:
                return False
            inStack.add(idx)
            for nhbr in dictn[idx]:
                if not Helper(nhbr):
                    return False
                     
            inStack.remove(idx)
            visited.add(idx)
            stack.append(idx)
            return True
        
        if numCourses == 0:
            return []
        if numCourses == 1:
            return prerequisites[0]
        dictn = defaultdict(list)
        for i in prerequisites:
            dictn[i[1]].append(i[0])
        visited = set()
        inStack = set()
        stack = []
        for idx in range(numCourses):
            if idx not in visited:
                if not Helper(idx):
                    return []
        return stack[::-1]
