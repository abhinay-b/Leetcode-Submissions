class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::deque<int> stack;
        string ops = "*/+-", token;
        int op1,op2;
        int findPos;
        for(int i = 0; i < tokens.size(); i++)
        {
            token = tokens[i];
            findPos = ops.find(token);
            if(findPos != string::npos)
            {
                op1 = stack.back();
                stack.pop_back();
                op2 = stack.back();
                stack.pop_back();
                switch(findPos)
                {
                    case 0: op2 *= op1; break;
                    case 1: op2 /= op1; break;
                    case 2: op2 += op1; break;
                    case 3: op2 -= op1; break;
                }
                stack.push_back(op2);
            }
            else
                stack.push_back(stoi(token));
        }
        return stack.back();
    }
};
