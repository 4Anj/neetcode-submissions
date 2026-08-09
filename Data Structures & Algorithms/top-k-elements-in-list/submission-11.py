class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        c=Counter(nums)
        b=[]
        for i,f in c.items():
            heapq.heappush(b,(f,i))
            if len(b)>k:
                heapq.heappop(b)
        return [i for f,i in b]