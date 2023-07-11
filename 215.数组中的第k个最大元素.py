#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
import random
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 整体思路，采用快排的思想，每次随机确定一个pivot，进行快排
        # 当pivot的index小于n-k时，再快排右边
        # 当pivot的index大于n-k时，快排左边
        # 当pivot的index等于n-k时，返回pivot

        # 定义快排函数
        def patition(left,right):
            # 随机选择一个pivot
            pivot_index = random.randint(left,right)
            # 将pivot放到最左边
            nums[pivot_index],nums[left] = nums[left],nums[pivot_index]
            # 定义当前位置的指针
            cur_index = left
            # 遍历数组，将小于pivot的数放到左边，大于pivot的数放到右边
            for i in range(left+1,right+1):
                if nums[i] < nums[left]:
                    cur_index+=1
                    nums[i],nums[cur_index] = nums[cur_index],nums[i]

            # 将pivot放到正确的位置
            nums[cur_index],nums[left] = nums[left],nums[cur_index]

            return cur_index

        # 获取数组长度
        n = len(nums)
        # 获取目标数的下标,因为是第k大的数，所以是n-k
        target_index = n - k

        # 定义左右指针,限定在左右边界内
        left = 0
        right = n-1
        # 进行快排
        while left <= right:# 这里要注意，是<=，因为当left=right时，还要进行一次快排
            #当left=right时，说明当前区间只有一个元素，这个元素就是pivot，此时需要将pivot放到正确的位置，
            #即cur_index，然后返回该数。因此，需要进行一次快排。
            #当区间是1个元素时，cur_index=left=right，这是一种极端情况，在最差的情况下，是最终答案，所以需要进行一次快排
            cur_index = patition(left,right)
            if cur_index==target_index:
                # 当找到目标数时，返回该数
                return nums[cur_index]
            elif cur_index<target_index:
                # 当pivot的index小于n-k时，再快排右边
                left = cur_index+1
            else:
                # 当pivot的index大于n-k时，快排左边
                right = cur_index-1

        

# @lc code=end

