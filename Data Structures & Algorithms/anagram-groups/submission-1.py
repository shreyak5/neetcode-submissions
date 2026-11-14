class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for ele in strs:
            s_ele = str(sorted(ele))
            if s_ele not in ans:
                ans[s_ele] = []
            ans[s_ele].append(ele)
        return [sublist for key, sublist in ans.items()]
    