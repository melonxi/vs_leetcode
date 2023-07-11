#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #先排序
        nums.sort()
        half = len(nums[::2])
        nums[::2],nums[1::2] = nums[:half][::-1],nums[half:][::-1]#之所以要[::-1]是因为正序可能会导致相同元素相邻
# @lc code=end

