"""
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        The idea is to go from left to right and find the minimum and update the minimum and profit
        """
        """
        Time complexity: O(N)
        Space complexity: O(1)
        """
        minimum = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if minimum > prices[i]:
                minimum = prices[i]
            
            if prices[i] - minimum > profit:
                profit = prices[i] - minimum

        return profit

if __name__ == '__main__':
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5
    assert Solution().maxProfit([7,6,4,3,1]) == 0
    assert Solution().maxProfit([7,6,4,3,1,9]) == 8

