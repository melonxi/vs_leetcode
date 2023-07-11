#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #双指针，一个在数组头，一个在数组尾巴。相向而行
        #时间复杂度O(n)
        #空间复杂度O(1)
        left = 0
        right = len(s) - 1
        while left < right: 
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
    
# @lc code=end

