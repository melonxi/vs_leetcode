#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        #动态规划
        #DP[i]代表凑成i所需的最少的完全平方数的和
        #DP[i] = min(DP[i],DP[i-num*num]+1),num*num需要小于i
        #DP[i]初始化为i
        #通过嵌套的遍历，得到答案
        dp = [i for i in range(n+1)]  # 初始化动态规划数组

    # 从小到大找所有的完全平方数，并更新 dp
        for i in range(2, n+1):
            for j in range(1,int(i**0.5)+1):
                
            #for j in range(1, int(i ** 0.5) + 1):
                    dp[i] = min(dp[i], dp[i - j*j] + 1)

        return dp[n]

       
# @lc code=end

