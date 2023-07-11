#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
from typing import List
from functools import cmp_to_key

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 1. 比较两个数的大小，如果ab > ba，则a > b
        # 2. 对数组进行排序
        # 3. 将数组中的元素拼接成字符串
        # 4. 注意：[0, 0] -> "00" -> "0"
        def compare(x: str, y: str) -> int:
            #如果y+x > x+y,则y在前
            return int(y + x) - int(x + y)
        # 1. 将数组中的元素转换成字符串
        # 2. 对字符串进行排序
        # 3. 将排序后的字符串拼接成一个字符串
        # 4. 注意：[0, 0] -> "00" -> "0"
        #cmp_to_key(compare) 将比较函数转换成key函数
        
        nums = sorted(map(str, nums), key=cmp_to_key(compare))
        #当第一位为0时，直接返回0
        return str(int(''.join(nums))) if nums[0] != '0' else '0'
        


       
# @lc code=end

