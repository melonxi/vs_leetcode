#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #动态规划
        #dp[i][0]表示以nums[i]结尾的连续子数组的最小值
        #dp[i][1]表示以nums[i]结尾的连续子数组的最大值
        #dp[i][0] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
        #dp[i][1] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
        #之所以要同时记录最大值和最小值，是因为负负得正，最小值乘以一个负数可能会变成最大值
        #时间复杂度O(n)，空间复杂度O(n)
        '''
        if not nums:
            return 0
        #初始化，dp[0][0]和dp[0][1]都为nums[0]，是因为只有一个元素的时候，最大值和最小值都是它自己
        dp = [[nums[j], nums[j]] for j in range(len(nums))]
        for i in range(1, len(nums)):
            dp[i][0] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
            dp[i][1] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
        return max([i[1] for i in dp])
        '''
        #根据滚动数组思想，可以将空间复杂度优化到O(1)
        max_value = nums[0]
        min_value = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):   
            temp = max_value
            max_value = max(max_value*nums[i], min_value*nums[i], nums[i])
            min_value = min(temp*nums[i], min_value*nums[i], nums[i])
            res = max(res, max_value)
        return res

       

# @lc code=end

