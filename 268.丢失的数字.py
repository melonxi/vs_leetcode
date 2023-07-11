#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #遍历一遍数组，将数组中的数字视为index,放在其对应的位置上
        #再遍历一遍数组，找到第一个不在其对应位置上的数字，返回其index
        for i in range(len(nums)):
            while nums[i] != i and nums[i] < len(nums):#注意这里的条件，nums[i] < len(nums)，否则会死循环
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)#如果数组中的数字都在其对应位置上，那么缺失的数字就是数组的长度
    
# @lc code=end

