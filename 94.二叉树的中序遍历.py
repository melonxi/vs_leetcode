#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        #回溯法,递归,时间复杂度O(n),空间复杂度O(n)
        #递归过程中,先遍历左子树,再遍历根节点,最后遍历右子树
        '''
        def DFS(node):
            if not node:
                return
            DFS(node.left)
            ans.append(node.val)
            DFS(node.right)
        DFS(root)
        return ans
        '''
        #迭代法,即为显式地使用栈,时间复杂度O(n),空间复杂度O(n)
        #迭代过程中,先遍历左子树,再遍历根节点,最后遍历右子树
        if not root:
            return []
        stack = []
        ans = []
        stack.append(root)
        while stack:
            #先遍历左子树
            while stack[-1].left:#如果左子树不为空,则一直遍历左子树
                stack.append(stack[-1].left)#将左子树入栈
            while stack:#如果左子树为空,则遍历根节点,再遍历右子树
                node = stack.pop()#将根节点出栈
                ans.append(node.val)#将根节点的值加入到ans中
                if node.right:#如果右子树不为空,则将右子树入栈
                    stack.append(node.right)#将右子树入栈
                    break#跳出循环,继续遍历右子树
        return ans

# @lc code=end

