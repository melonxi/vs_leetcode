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
        

        num_index_dict = {}# key: num, value: index
        for i,num in enumerate(nums):# 遍历数组
            if target - num in num_index_dict:# 如果target - num在哈希表中
                return [i,num_index_dict[target - num]]# 返回下标
            else:
                num_index_dict[num] = i# 否则将num存入哈希表
        
                        
# @lc code=end

