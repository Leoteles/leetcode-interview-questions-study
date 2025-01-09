#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
#9:06
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices = [7,1,5,3,6,4]
        profit = 0
        buy = 0
        for sell in range(1,len(prices)):
            if prices[sell] > prices[buy]:
                profit += prices[sell] - prices[buy]
            buy = sell
        return profit    