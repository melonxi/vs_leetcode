#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #哈希表+排序
        check = {}
        for s in strs:
            key = tuple(sorted(s))#tuple是不可变的，可以作为字典的key
            check[key] = check.get(key, []) + [s]
        return list(check.values())
    
# @lc code=end

