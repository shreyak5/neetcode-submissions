class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        
        ans = 0
        for n in nums:
            if n not in numbers:
                continue
            
            count = 1
            # check ahead of it
            curr = n + 1
            while curr in numbers:
                count += 1
                numbers.remove(curr)
                curr += 1
                
            # check behind of it
            curr = n - 1
            while curr in numbers:
                count += 1
                numbers.remove(curr)
                curr -= 1

            ans = max(count, ans)

        return ans

        