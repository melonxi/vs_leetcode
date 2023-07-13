#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 二分查找，其思路和一般的二分查找不同，这里的二分查找是对值进行二分查找，而不是对索引进行二分查找
        #查找的区间是[1,n]，而不是[0,n-1]
        #理论上不重复的话，每个数都是唯一的，所以如果小于等于mid的数的个数大于mid，那么重复的数就在[1,mid]之间
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        return right#最后left和right都是一样的，所以返回哪个都可以
       
    
# @lc code=end

