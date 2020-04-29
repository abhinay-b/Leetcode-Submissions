class Solution {
    bool helper(vector<vector<char>>& board, int i,int j, string word, int index)
    {
        if(index == word.size()-1)
            return true;
        auto temp = board[i][j];
        board[i][j] = '$';
        vector<pair<int,int>> nhbrs = {{i-1,j},{i+1,j},{i,j+1},{i,j-1}};
        for(auto &[p,q]:nhbrs)
        {
            if( (0 <= p && p < board.size()) && (0 <= q && q < board[0].size()) && 
                (board[p][q] == word[index+1]))
            {
                if(helper(board,p,q,word,index+1))
                    return true;
            }
        }
        board[i][j] = temp;
        return false;
    }
public:
    bool exist(vector<vector<char>>& board, string word) 
    {        
        for(int i = 0; i < board.size();i++)
        {
            for(int j = 0; j < board[i].size();j++)
            {
                if(board[i][j] == word[0])
                {
                    if(helper(board, i, j, word, 0))
                        return true;
                }
            }
        }
        return false;
    }
};
