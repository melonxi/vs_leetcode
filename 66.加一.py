#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #由于题目没有说明时间复杂度的要求，因此在处理最高位进位时，可以使用python的特性，直接数组插入1
        #定义一个进位标志carry，初始值为1，表示最低位加1
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+carry==10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += carry
                return digits
        digits.insert(0,1)
        return digits
# @lc code=end

