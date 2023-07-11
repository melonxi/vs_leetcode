#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #回溯，DFS
        ans = []
        def backtrack(nums,cur):
            if not nums:
                ans.append(cur)
                return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],cur+[nums[i]])    
        backtrack(nums,[])
        return ans
    

# @lc code=end

