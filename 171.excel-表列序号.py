#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        #哈希表记录字母和数字的对应关系
        #从右往左遍历，每次遍历到一个字母，就将其对应的数字加到结果中，从右往左进位是乘26，也就是最低位乘1，次低位乘26，再次低位乘26的平方
        #注意：这里的进位是从右往左进位，而不是从左往右进位
        alpha_num = {}
        for i in range(26):
            alpha_num[chr(ord('A') + i)] = i + 1#ord()返回字符的ASCII码，chr()返回ASCII码对应的字符
        res = 0
        for i in range(len(columnTitle)-1,-1,-1):
            res+=alpha_num[columnTitle[i]]*26**(len(columnTitle)-i-1)
        return res
    
# @lc code=end

