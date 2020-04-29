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
                while  count1 > 0 and i >= 0:
                    if S[i] == '#':
                        count1 += 1
                    else:
                        count1 -= 1
                    i -= 1
                while  count2 > 0 and j >= 0:
                    if T[j] == '#':
                        count2 += 1
                    else:
                        count2 -= 1
                    j -= 1
            elif i < 0 or j < 0 or S[i] != T[j]:
                return False
            else:
                i -= 1
                j -= 1
        return True
