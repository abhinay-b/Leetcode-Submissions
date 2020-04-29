from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def Helper(idx):
            if idx in visited:
                return True 
            if idx in stack:
                return False
            stack.add(idx)
            for j in dictn[idx]:
                if not Helper(j):
                    return False
            stack.remove(idx)
            visited.add(idx)
            return True
        
        if numCourses < 2:
            return True
        visited = set()
        stack = set()
        dictn = defaultdict(list)
        for i in prerequisites:
            dictn[i[1]].append(i[0])
        for i in range(numCourses):                       
            if not Helper(i):
                return False
        return True
    
        
