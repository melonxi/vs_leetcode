#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #原地hash，index是从0开始的，每个index都尽量填充index+1的数
        #完成遍历填充之后，再次遍历，当发现nums[index]!=index+1时输出index+1
        #如果都对应就输出列表长度加1
        #重点是原地hash的过程，在遍历每个位置是，需要在循环内部进行一个位置替换的循环，即
        #当0<nums[i]<=len(nums)时，把nums[i]和nums[nums[i]-1]进行交换，直到不符合判断条件再跳出
        if not nums:
            return 1
        n = len(nums)
        for i in range(n):
            while 0<nums[i]<=len(nums) and nums[nums[i] - 1] != nums[i] and nums[i]!=i+1:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                #nums[i],nums[nums[i] - 1] = nums[nums[i]-1],nums[i]
        
        for index in range(n):
            if nums[index]!=index+1:
                return index+1
        return n+1

        



# @lc code=end

