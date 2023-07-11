#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        #双指针，从左端点和右端点相向逼近，移动长度短的指针，维护一个最大值
        left= 0
        right = len(height)-1
        max_area = 0
        while left < right:
            if (right-left)*min(height[left],height[right]) > max_area:
                max_area = (right-left)*min(height[left],height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
# @lc code=end

