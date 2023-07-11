#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hash
        #如果字符串长度不一样，直接返回False
        #遍历字符串s，将每个字符作为键，出现的次数作为值，存入字典
        #遍历字符串t，如果字符不在字典中，返回False，如果在字典中，将值减一,如果值小于0，返回False
    

        help_dict = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in help_dict:
                help_dict[i] = 1
            else:
                help_dict[i] += 1
        for j in t:
            if j not in help_dict:
                return False
            else:
                help_dict[j] -= 1
                if help_dict[j] < 0:
                    return False
        return True
    
        
            
        

# @lc code=end

