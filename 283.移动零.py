#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i+=1
        for j in range(i,len(nums)):    
            nums[j] = 0
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
# @lc code=end

