#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #双指针，快慢指针
        #如果快指针和慢指针的值相同，快指针向前走一步
        #如果快指针和慢指针的值不同，慢指针向前走一步，然后把快指针的值赋给慢指针
        #慢指针加1，不会覆盖掉前面的值，因为前面的值都是相同的
        #最后返回慢指针的下标+1
        if not nums:
            return 0
        slow = 0
        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow+1
    
# @lc code=end

