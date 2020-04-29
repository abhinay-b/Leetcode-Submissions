class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        connected=set()
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
                connected.add((i,j))
                if i-1 > 0 and board[i-1][j] == 'O' and (i-1,j) not in connected:
                    queue.append((i-1,j))
                if i+1 < m and board[i+1][j] == 'O' and (i+1,j) not in connected:
                    queue.append((i+1,j))
                if j-1 > 0 and  board[i][j-1] == 'O' and (i,j-1) not in connected:
                    queue.append((i,j-1))
                if j+1 < n and board[i][j+1] == 'O' and (i,j+1) not in connected:
                    queue.append((i,j+1))
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in connected:
                    board[i][j] = 'X'
