class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0          # Buy day (lowest price seen so far)
        profit = 0        # Maximum profit found

        for right in range(1, len(prices)):  # Sell day

            # Found a cheaper day to buy
            if prices[right] < prices[left]:
                left = right

            # Otherwise, calculate profit if we sell today
            else:
                current_profit = prices[right] - prices[left]
                profit = max(profit, current_profit)

        return profit