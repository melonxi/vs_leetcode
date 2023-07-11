#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #递归
        # 1.递归函数的返回值应该是什么？
        # 2.递归终止条件是什么？
        # 3.单层递归逻辑应该是什么？
        self.maxSum = float('-inf')
        def dfs(root):
            if not root:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            self.maxSum = max(self.maxSum, left + right + root.val)#维护一个当前最大值，也就是说当前节点不一定会向上层递归提供贡献值
            #返回当前节点的最大贡献值，也就是说当前节点会继续向上层递归提供贡献值
            return max(left, right) + root.val
        dfs(root)
        return self.maxSum
    
# @lc code=end

