class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        maxar = 0
        while left < right :
            width = right - left 
            watheight = min (height[left] , height [right])
            ar = width * watheight
            maxar = max(maxar, ar)
            if height [left] < height[right]:
                left+=1
            else:
                right -=1
        return maxar

        