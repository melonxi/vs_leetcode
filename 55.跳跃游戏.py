#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #贪心法，维护一个最大可达距离，如果当前位置超过了最大可达距离，返回False
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach,i+nums[i])#更新最大可达距离
        return True
    


    
# @lc code=end

