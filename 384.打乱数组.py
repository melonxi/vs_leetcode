#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
import random
class Solution:
    #初始化时保存原始数组
    #重置时恢复原始数组
    #打乱时遍历数组，每次从当前位置到最后位置随机选择一个元素与当前位置元素交换

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)


    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original
        self.original = list(self.original)
        return self.nums


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        #遍历数组，每次从当前位置到最后位置随机选择一个元素与当前位置元素交换
        for i in range(len(self.nums)):
            swap_idx = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]
        return self.nums



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

