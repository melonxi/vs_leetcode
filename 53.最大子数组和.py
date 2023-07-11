#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #动态规划解法
        #dp[i]表示以nums[i]结尾的最大子数组和   
        #由于我们设定的dp[i]表示以nums[i]结尾的最大子数组和，所以dp[i]只能由dp[i-1]转移得到，或者nums[i]本身就是最大子数组和
        #且dp[i-1]代表的是以nums[i-1]结尾的最大子数组和，所以dp[i-1]已经是以i-1为结尾的最大值，所以如果dp[i-1]为负数，那么dp[i-1]+nums[i]肯定比nums[i]小，所以dp[i] = nums[i]
        #dp[i] = max(dp[i-1]+nums[i],nums[i])   
        #dp[0] = nums[0]
        #最终结果是max(dp)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)
    
# @lc code=end

