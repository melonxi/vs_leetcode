#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #两次遍历，一次哈希表，一次遍历
        dic = {}
        for i in nums1:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        res = []
        for i in nums2:
            if i in dic and dic[i]>0:
                res.append(i)
                dic[i]-=1
        return res
    
# @lc code=end

