class Solution:
    def convert(self, s: str, rows: int) -> str:
        substrLists = [[] for i in range(rows)]
        start = 0
        end = rows - 1

        strLen = len(s) - 1
        offset = 2*rows - 2
        round = 1
        deadend = False
        if strLen < 0:
            deadend = True
            return ""
        if rows == 1:
            return s
        for i in range(rows):
            substrLists[i] = [i]
            if i == strLen:
                deadend = True
                break


        while deadend == False:
            if round % 2 == 0:    
                temp = substrLists[start][-1] + offset
                if strLen >= temp:
                    substrLists[start].append(temp)
                if strLen == temp:
                    break
                
                temp = substrLists[end][-1] + offset
                if strLen >= temp:
                    substrLists[end].append(temp)
                if strLen == temp:
                    break
                    
            for i in range(1,rows-1): 
                if round % 2 > 0:
                    temp = substrLists[end][-1] + rows - i - 1
                else:
                    temp = substrLists[0][-1] + i
                
                if temp <= strLen:
                    substrLists[i].append(temp)
                if temp == strLen:
                    deadend = True
                    break

            round += 1

    #     print("substrLists",substrLists)
        result = ""
        for charList in substrLists:
            for i in charList:
                result += s[i]
        return result
