class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0
        while(left < right):
            diff = right - left
            if(height[left] < height[right]):                
                minHeight = height[left]
                left += 1
            else:                
                minHeight = height[right]
                right -= 1
            temp = diff * minHeight
            maxarea = max(temp,maxarea)
        return maxarea
        
