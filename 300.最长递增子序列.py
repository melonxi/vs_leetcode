#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #动态规划，DP[i]代表当前index的最长递增子序列的长度
        #DP[i] = max(DP[j]) + 1, j < i and nums[j] < nums[i]
        #即nums[i]>nums[j]时，DP[i] = max(DP[j]) + 1
        #时间复杂度O(n^2)，空间复杂度O(n)
        if not nums:
            return 0
        DP = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    DP[i] = max(DP[i], DP[j] + 1)
        return max(DP)
    

    
# @lc code=end

