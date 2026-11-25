class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0]*n
        for i in range(n - 1, -1, -1):
            while stack:
                top_idx = stack[-1]
                if temperatures[top_idx] > temperatures[i]:
                    ans[i] = top_idx - i
                    break
                stack.pop(-1)
            
            stack.append(i)
        
        return ans
        
        

        