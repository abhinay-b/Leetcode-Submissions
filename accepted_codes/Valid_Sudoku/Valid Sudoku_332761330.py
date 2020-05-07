from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = set()
        colSets = [set() for i in range(9)]
        boxList = [[None]*9 for _ in range(9)]
        for i in range(9):
            rowSet.clear()
            for j in range(9):
                temp = board[i][j]
                if temp == ".":
                    continue
                if (temp in rowSet) or (temp in colSets[j]) or (temp in boxList[3*(i//3) + (j 
                    // 3)]):
                    return False
                rowSet.add(temp)
                colSets[j].add(temp)
                boxList[3*(i//3)+(j//3)].append(temp)
        return True
