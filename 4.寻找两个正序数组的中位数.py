#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 获取两个数组的总长度
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2

        # 如果总长度是偶数，需要找到中间的两个数
        if n % 2 == 0:
            # 求解第k小数，k为总长度的一半
            left = self.findKth(nums1, nums2, n // 2)
            right = self.findKth(nums1, nums2, n // 2 + 1)
            return (left + right) / 2.0
        # 如果总长度是奇数，直接找到中间的数
        else:
            return self.findKth(nums1, nums2, n // 2 + 1)

    def findKth(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 如果其中一个数组已经为空，直接返回另一个数组的第k小数
        if not nums1:
            return nums2[k - 1]
        if not nums2:
            return nums1[k - 1]
        
        # 如果k=1，返回两个数组中最小的数
        if k == 1:
            return min(nums1[0], nums2[0])
        
        # 将k分成两部分
        i = min(k // 2, len(nums1))
        j = min(k-i, len(nums2))

        # 如果nums1[i-1]小于nums2[j-1]，则第k小数不可能在nums1的前i个数中，将nums1的前i个数舍去，继续寻找
        if nums1[i - 1] < nums2[j - 1]:
            return self.findKth(nums1[i:], nums2, k - i)
        # 如果nums2[j-1]小于nums1[i-1]，则第k小数不可能在nums2的前j个数中，将nums2的前j个数舍去，继续寻找
        else:
            return self.findKth(nums1, nums2[j:], k - j)

# @lc code=end

