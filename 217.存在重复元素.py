#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #哈希表，遍历数组，如果哈希表中存在该元素，则返回True，否则将该元素加入哈希表
        check_dict = set()
        for num in nums:
            if num in check_dict:
                return True
            else:
                check_dict.add(num)
        return False
# @lc code=end

