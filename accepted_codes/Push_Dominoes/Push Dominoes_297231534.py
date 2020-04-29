class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if len(dominoes) <= 1:
            return dominoes
        i = 0
        stats = []
        res = ''
        while i < len(dominoes):
            if dominoes[i] == 'R':
                i += 1
                stats.append(['R',1])
                count = 1
                while i < len(dominoes) and dominoes[i] == '.':
                    count += 1
                    stats.append(['R',count])
                    i += 1
            elif dominoes[i] == 'L':
                j = i-1
                i += 1
                stats.append(['L',1])
                count = 1
                while j >= 0 and (stats[j][0] == '.' or (stats[j][0] == 'R' and stats[j][1] > 
                    count+1)):
                    count += 1
                    stats[j][0] = 'L'
                    stats[j][1] = count
                    j -= 1
                if j >= 0 and stats[j][0] == 'R' and stats[j][1] == count+1:
                    stats[j][0] = '.'
                    stats[j][1] = 1
            else:
                stats.append(['.',1])
                i += 1
        for stat in stats:
            res += stat[0]
        return res
