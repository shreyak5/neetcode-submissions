class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            ans = max(ans, (j - i) * min(heights[i], heights[j]))
            if i + 1 == j:
                break
            if heights[i] > heights[j]:
                j -= 1
            elif heights[j] > heights[i]:
                i += 1
            else:
                if heights[i + 1] > heights[j - 1]:
                    i += 1
                else:
                    j -= 1
    
        return ans