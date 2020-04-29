from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> 
        List[List[int]]:
        if not image or not image[0]:
            return image
        queue = deque([(sr,sc)])
        
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        image[sr][sc] = newColor
        while queue:
            print(queue)
            row,col = queue.popleft()
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0 <= (row+i) < len(image) and 0 <= (col+j) < len(image[0]) and image[row
                    +i][col+j] == oldColor:
                    image[row+i][col+j] = newColor
                    queue.append((row+i,col+j))
        return image
