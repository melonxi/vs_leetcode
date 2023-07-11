#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #动态规划
        if not prices:
            return 0
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,len(dp)):
            #第i天不持有股票存在两种可能性，前一天不持有股票，今天不买入，前一天持有股票，今天卖出
            #第i天持有股票存在两种可能性，前一天持有股票，今天不卖出，前一天不持有股票，今天买入
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][0]-prices[i],dp[i-1][1])
        return dp[-1][0]
    

# @lc code=end

