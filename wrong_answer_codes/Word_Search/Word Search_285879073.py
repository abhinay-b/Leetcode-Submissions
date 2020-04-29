class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board,i,j,visited,wordLeft):            
            if board[i][j] != wordLeft[0] or visited[i][j]:
                return False
            
            if len(wordLeft) == 1:
                return True
            
            visited[i][j] = True
            up = down = left = right = False
            
            if i > 0:
                up = dfs(board,i-1,j,visited,wordLeft[1:])
            if i < len(board)-1:
                down = dfs(board,i+1,j,visited,wordLeft[1:])
            if j > 0:
                left = dfs(board,i,j-1,visited,wordLeft[1:])
            if j < len(board[0])-1:
                right = dfs(board,i,j+1,visited,wordLeft[1:])
            return (up or down or left or right)
        
        if len(board) == 0 or len(board[0]) == 0:
            return False
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visitNode = [[False]*len(board[0]) for _ in range(len(board))]
                if board[i][j] == word[0]:
                    temp = dfs(board,i,j,visitNode,word)
                    if temp == True:
                        return True
        return False
                       
