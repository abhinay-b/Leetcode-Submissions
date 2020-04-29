class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = []
        if not board or not board[0]:
            return
        m,n = len(board), len(board[0])
        for j in range(n):
            if board[0][j] == 'O':
                queue.append((0,j))
            if board[m-1][j] == 'O':
                queue.append((m-1,j))
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i,0))
            if board[i][n-1] == 'O':
                queue.append((i,n-1))
        while queue:
                i,j = queue.pop(0)
                board[i][j] = 'C'
                for idx1,idx2 in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0 < idx1 < m-1 and 0 < idx2 < n-1 and board[idx1][idx2] == 'O':
                        queue.append((idx1,idx2))
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'C':
                    board[i][j] = 'O'
