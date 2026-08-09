class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        mp=float("-inf")
        m=float("inf")
        for i in prices:
            if m>i:
                m=i
            mp=i-m
            p=max(p,mp)
        return p