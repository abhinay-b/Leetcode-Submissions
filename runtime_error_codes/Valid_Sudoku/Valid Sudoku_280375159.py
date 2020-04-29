from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for lst in board:
            ctr = Counter(lst)
            del ctr['.']
            if len(ctr) == 0:
                return True
            if ctr.most_common(1)[0][1] > 1:
                return False
        for i in range(len(board)):
            lst = [board[i][j] for j in range(len(board))]
            ctr = Counter(lst)
            del ctr['.']
            if ctr.most_common(1)[0][1] > 1:
                return False
        lst = [[] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                lst[3*(i // 3) + (j // 3)].append(board[i][j])
        for l in lst:
            ctr = Counter(l)
            del ctr['.']
            if ctr.most_common(1)[0][1] > 1:
                   return False
        return True
