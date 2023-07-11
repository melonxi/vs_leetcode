#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #二分查找的变形
        #排序过的旋转数组，经过二分，仍然会有一般是有序的
        #通过比较nums[mid]的值和nums[low]，以及nums[high]的值
        #可以判断，现阶段左右哪边是有序数组
        low = 0
        high = len(nums)-1
        while low <= high:
            mid  = (low+high)//2#
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[low]:#mid坐标及其左边是有序的
                if nums[mid]>target and nums[low]<=target:
                    high = mid-1
                else:
                    low = mid+1
            else:#mid坐标及其右边是有序的
                if nums[high]>=target and nums[mid]<target:
                    low = mid+1
                else:
                    high = mid-1
        return -1


# @lc code=end

