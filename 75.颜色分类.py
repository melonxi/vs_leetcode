#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 双指针,左指针指向0的最右边界，右指针指向2的最左边界
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        left = 0
        right = len(nums) - 1
        i = 0   
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
        """
        Do not return anything, modify nums in-place instead.
        """
# @lc code=end

