class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i1, n1 in enumerate(nums):
            n2 = target - n1
            if n2 in check:
                i2 = check[n2]
                return [i2, i1]
            check[n1] = i1 



        