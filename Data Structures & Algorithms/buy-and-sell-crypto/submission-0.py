class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #keep track of lowest price so far
        #best profit so far

        lowest = prices[0]
        best_profit = 0

        for p in prices:
            lowest = min(p,lowest)
            profit = p - lowest 
            best_profit = max(best_profit, profit)
        return best_profit