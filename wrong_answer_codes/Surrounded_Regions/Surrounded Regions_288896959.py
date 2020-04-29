class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        connected=set()
        if not board or not board[0]:
            return
        m,n = len(board), len(board[0])
        for j in range(n):
            if board[0][j] == 'O':
                connected.add((0,j))
            if board[m-1][j] == 'O':
                connected.add((m-1,j))
        for i in range(m):
            if board[i][0] == 'O':
                connected.add((i,0))
            if board[i][n-1] == 'O':
                connected.add((i,n-1))
        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j] == 'O':
                    if (i-1,j) in connected or (i+1,j) in connected or (i,j-1) in connected or 
                        (i,j+1) in connected:
                        connected.add((i,j))
                    else:
                        board[i][j] = 'X'
        
