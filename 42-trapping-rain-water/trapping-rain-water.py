class Solution(object):
    def trap(self, height):
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r] 
        water = 0
        while l < r: 
          if leftMax <= rightMax:
            water += leftMax - height[l] 
            l += 1
            leftMax = max(leftMax, height[l])
          else:
            water += rightMax - height[r]
            r -= 1
            rightMax = max(rightMax, height[r])
        return water