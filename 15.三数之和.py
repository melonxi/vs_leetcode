#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        if not nums or n<3:
            return []
        nums.sort()

        ans = []
        for left in range(n):
            if nums[left] > 0:
                return ans

            if left > 0 and nums[left] == nums[left-1]:
                continue
            middle = left + 1
            right = n-1
            
            while middle < right:
                if nums[left]+nums[middle]+nums[right]==0:
                    ans.append([nums[left],nums[middle],nums[right]])
                    while middle < right and nums[right]==nums[right-1]:
                        right-=1
                    right-=1
                    while middle < right and nums[middle]==nums[middle+1]:
                        middle+=1
                    middle+=1
                elif nums[left]+nums[middle]+nums[right]>0:
                    right-=1
                else:
                    middle+=1
                        
        return ans

# @lc code=end

