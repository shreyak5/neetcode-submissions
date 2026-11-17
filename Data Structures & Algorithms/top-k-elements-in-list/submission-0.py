class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        
        sorted_freq = sorted(freq.items(), reverse=True, key=lambda kv: kv[1])
        return [ele for ele, f in sorted_freq][:k]