class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=prices[0];a=0
        for i in range(1,len(prices)):
            if prices[i]<p:
                p=prices[i]
            else:
                ans=prices[i]-p
                a=max(a,ans)
        return a

        