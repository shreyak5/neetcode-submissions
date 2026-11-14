class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # O(n*m), O(m)
        ans = {}
        for ele in strs:
            s_ele = list(ele)
            s_ele.sort()
            s_ele = str(s_ele)
            if s_ele not in ans:
                ans[s_ele] = []
            ans[s_ele].append(ele)
        return [sublist for key, sublist in ans.items()]
    