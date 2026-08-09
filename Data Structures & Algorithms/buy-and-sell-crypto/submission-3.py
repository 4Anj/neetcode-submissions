class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        m=prices[0]
        for i in prices:
            m=min(m,i)
            p=max(p,i-m)
        return p