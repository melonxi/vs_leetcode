 #
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #动态规划，前i天的最大利润 = max(前i-1天的最大利润，第i天的价格-前i-1天中的最小价格)
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit,price-min_price)
        
        return max_profit

# @lc code=end

