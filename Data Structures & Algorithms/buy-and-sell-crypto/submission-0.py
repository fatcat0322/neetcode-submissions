class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=101
        profit=0
        for p in prices:
            buy=min(p,buy)
            profit=max(p-buy,profit)
        return profit