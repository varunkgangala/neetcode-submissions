class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        max_prof=0
        for right in range(1,len(prices)):
            if prices[right]>prices[left]:
                prof=prices[right]-prices[left]
                max_prof=max(prof,max_prof)
            else:
                left=right
        return max_prof
            
