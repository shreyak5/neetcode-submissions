class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        target = 0
        ans = []
        for beg in range(n):
            curr_target = target - nums[beg]
            i = beg + 1
            j = n - 1
            while i < j:
                curr_sum = nums[i] + nums[j]
                if curr_sum > curr_target:
                    j -= 1
                elif curr_sum < curr_target:
                    i += 1
                else:
                    ans.append((nums[beg], nums[i], nums[j]))
                    i += 1
                    j -= 1
    
        return [list(s) for s in set(ans)]


        