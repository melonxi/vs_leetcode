#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 使用哈希表，时间复杂度O(n)，空间复杂度O(n)
        # 哈希表存储每个数字的下标
        

        num_index_dict = {}
        for i,num in enumerate(nums):
            if target - num in num_index_dict:
                return [i,num_index_dict[target - num]]
            else:
                num_index_dict[num] = i
        
                        
# @lc code=end

