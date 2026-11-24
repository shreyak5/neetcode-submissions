class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1:
            return 0
        right_wall = [0]*n

        # calculate right wall
        for i in range(n - 2, -1, -1):
            right_wall[i] = max(right_wall[i + 1], height[i + 1])
        
        ans = 0
        left_wall = height[0]
        # calculate left wall and ans
        for i in range(1, n):
            ans += max(0, (min(right_wall[i], left_wall)) - height[i])
            left_wall = max(left_wall, height[i])
        
        return ans
        
        