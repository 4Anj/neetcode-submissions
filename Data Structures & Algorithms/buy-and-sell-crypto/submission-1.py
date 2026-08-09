class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        m=prices[0]
        for i in prices:
            if m>i:
                m=i
            mp=i-m
            p=max(p,mp)
        return p