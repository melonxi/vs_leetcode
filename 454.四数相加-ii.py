#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        #四个数组找和为0，也就是寻找两两数组的相反数
        #将两两数组的和存入字典，key为和，value为出现次数
        #遍历两个字典，如果两个key相加为0，则将两个value相乘，即为结果
        #时间复杂度O(n^2)，空间复杂度O(n^2)
        dic1 = {}
        dic2 = {}
        for i in nums1:
            for j in nums2:
                if i+j in dic1:
                    dic1[i+j] += 1
                else:
                    dic1[i+j] = 1
        for i in nums3:
            for j in nums4:
                if i+j in dic2:
                    dic2[i+j] += 1
                else:
                    dic2[i+j] = 1
        res = 0
        for i in dic1:
            if -i in dic2:
                res += dic1[i] * dic2[-i]
        return res
    
# @lc code=end

