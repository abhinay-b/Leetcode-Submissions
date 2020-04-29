class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]:
            return -1
        m,n = len(dungeon),len(dungeon[0])
        dungeon[m-1][n-1] = max(1,1-dungeon[m-1][n-1])
        for i in range(len(dungeon)-2,-1,-1):
            dungeon[i][n-1] = max(1,dungeon[i+1][n-1]-dungeon[i][n-1])
        for j in range(len(dungeon[0])-2,-1,-1):
            dungeon[m-1][j] = max(1,dungeon[m-1][j+1]-dungeon[m-1][j])
        for i in range(len(dungeon)-2,-1,-1):
            for j in range(len(dungeon[0])-2,-1,-1):
                   dungeon[i][j] = max(1,min(dungeon[i+1][j],dungeon[i][j+1])-dungeon[i][j])
        return dungeon[0][0]
