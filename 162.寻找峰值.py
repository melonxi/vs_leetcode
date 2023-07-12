#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #不使用暴力法，使用二分查找的原因是因为题目要求时间复杂度为O(logN)
        #二分查找的思路是，如果nums[mid] < nums[mid+1]，则说明峰值在右边，反之在左边
        #因为题目要求返回任意一个峰值，所以不需要考虑边界条件
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        #返回left或者right都可以，因为最后left和right都会指向同一个位置
        return left

# @lc code=end

