class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i,j = len(S)-1,len(T)-1
        count1,count2 = 0,0
        while i >= 0 or j >= 0:
            if (i >= 0 and S[i] == '#') or (j >=0 and T[j] == '#'): 
                if i >= 0 and S[i] == '#':
                    i -= 1
                    count1 += 1                
                if j >=0 and T[j] == '#':
                    j -= 1
                    count2 += 1               
            elif count1 > 0 or count2 > 0:
                i -= count1
                count1 =0
                j -= count2
                count2 =0
            elif i < 0 or j < 0 or S[i] != T[j]:
                return False
            else:
                i -= 1
                j -= 1
        return True
