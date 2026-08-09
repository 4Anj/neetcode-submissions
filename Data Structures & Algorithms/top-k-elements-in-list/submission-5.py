class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c=Counter(nums)
        b=c.most_common(k)
        return [i for i,f in b]