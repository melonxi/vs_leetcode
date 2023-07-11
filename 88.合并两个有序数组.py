#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #逆序遍历+双指针
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return nums1
        
        n -= 1
        m -= 1
        for i in range(m+n+1,-1,-1):
            if nums1[m]>nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            if m<0 or n<0:  
                break
            
        #if n>=0:#如果nums2还有剩余，说明nums1已经遍历完了，直接把nums2剩余的元素放到nums1前面
        #当n小于0时，做赋值操作不会报错，因为n的最小可能值为-1，在进行赋值操作时，会先把n+1，因此等于没有赋值操作
        nums1[:n+1] = nums2[:n+1]
        #return nums1
    
# @lc code=end

