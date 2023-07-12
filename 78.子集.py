#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #DFS,每一步都保存,且DFS只遍历其后的元素，避免了重复
        n = len(nums)
        res = []
        def DFS(index,cur):
            res.append(cur)
            for i in range(index,n):
                DFS(i+1,cur+[nums[i]])
        DFS(0,[])

        return res
            

# @lc code=end

