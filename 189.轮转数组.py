#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #假设共n个元素
        #1.将前n-k个元素倒转
        #2.将后k个元素倒转
        #3.将所有元素倒转
        #注意k可能大于n，所以要取余
        n = len(nums)
        k = k % n
        left = 0
        right = n - k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -=1
        left = n - k
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -=1
        left = 0
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -=1
        """
        Do not return anything, modify nums in-place instead.
        """
# @lc code=end

