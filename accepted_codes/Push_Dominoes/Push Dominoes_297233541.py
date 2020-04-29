class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if len(dominoes) <= 1:
            return dominoes
        res = ''
        length = 0
        rightFall = False
        for i in dominoes:
            if i == '.':
                length += 1
                continue
            
            if i == 'R':
                
                if rightFall:
                    res += 'R'*length
                else:
                    res += '.'*length                    
                    rightFall = True
                res += i
            elif i == 'L':
                if rightFall:
                    res += 'R'*(length//2)
                    if length%2:
                        res += '.'
                    res += 'L'*(length//2)
                else:
                    res += 'L'*length
                res += i
                rightFall = False
            length = 0
        if length:
            if rightFall:
                res += 'R'*length
            else:
                res += '.'*length
        return res
