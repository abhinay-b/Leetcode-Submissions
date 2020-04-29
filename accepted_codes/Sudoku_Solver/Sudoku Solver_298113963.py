class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowSet = []
        colSet = []
        boxSet = []
        for i,row in enumerate(board):
            rowSet.append(set())
            for j,col in enumerate(row):
                if len(colSet) < j+1:
                    colSet.append(set())
                idx = 3*(i//3) + j//3
                if len(boxSet) < idx+1:
                    boxSet.append(set())
                if col == '.':
                    continue
                rowSet[i].add(col)
                colSet[j].add(col)
                boxSet[idx].add(col)
        def solve(i,j,m,n):
            if i == m:
                return True
            col = board[i][j]
            if col == '.':
                idx = 3*(i//3) + j//3
                for num in range(1,10):
                    num = str(num)
                    if num not in rowSet[i] and num not in colSet[j] and num not in 
                        boxSet[idx]:
                        board[i][j] = num
                        rowSet[i].add(num)
                        colSet[j].add(num)
                        boxSet[idx].add(num)
                        x,y = i,j+1
                        if y == n:
                            x += 1
                            y = 0
                        res = solve(x,y,m,n)
                        if res:
                            return res
                        board[i][j] = '.'
                        rowSet[i].remove(num)
                        colSet[j].remove(num)
                        boxSet[idx].remove(num)
                    else:
                        continue
            else:
                x,y = i,j+1
                if y == n:
                    x += 1
                    y = 0
                res = solve(x,y,m,n)
                if res:
                    return res

            if board[i][j] == '.':
                return False
        solve(0,0,len(board),len(board[0]))
