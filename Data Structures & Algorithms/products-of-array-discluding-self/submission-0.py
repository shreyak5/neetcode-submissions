class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0]*n
        ans = [0]*n

        left[0] = 1
        for i in range(1, n):
            left[i] = left[i - 1]*nums[i - 1]
            if left[i] == 0:
                break

        ans[n - 1] = left[n - 1]
        right = nums[n - 1]
        for i in range(n - 2, -1, -1):
            ans[i] = left[i]*right
            right *= nums[i]
            if right == 0:
                break
        
        return ans
        