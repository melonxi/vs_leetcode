#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       #思路：
       #数组中除去自身以外的所有数的乘积，可以转换为该数左边所有数的乘积 * 该数右边所有数的乘积
       #当前数左边的数的乘积，等于该数左边第一个数的左边的数的乘积 * 该数左边第一个数，因此
       #可以通过遍历数组，将当前数左边的数的乘积存储在数组中，然后再遍历数组，将当前数右边的数的乘积
         #乘以当前数左边的数的乘积，即为结果

        
        #一次遍历
        n = len(nums)
        res = [1] * n
        left = 1
        right = 1
        for i in range(n):
            res[i] *= left
            left *= nums[i]
            res[n-1-i] *= right
            right *= nums[n-1-i]
        return res



# @lc code=end


