#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        #动态规划,记录到达每个房子时偷或者不偷的最大值
        #dp[i][0]表示不偷第i个房子的最大值
        #dp[i][1]表示偷第i个房子的最大值
        #dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        #dp[i][1] = dp[i-1][0] + nums[i]
        #时间复杂度O(n)，空间复杂度O(n)
        
        if not nums:
            return 0
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] =  dp[i-1][0] + nums[i]
        return max(dp[n-1][0], dp[n-1][1])
    
# @lc code=end

