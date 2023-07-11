#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #通过先序遍历确定根节点，映射到中序遍历的根节点
        #中序遍历根节点的左边就是左子树，右边就是右子树
        #通过中序遍历确定左子树的长度，映射到先序遍历的左子树
        #通过中序遍历确定右子树的长度，映射到先序遍历的右子树
        #递归
        if not preorder or not inorder:#递归终止条件，当先序遍历或者中序遍历为空时，返回None
            return None
        root = TreeNode(preorder[0])#先序遍历的第一个节点就是根节点
        mid = inorder.index(preorder[0])#找到根节点在中序遍历中的位置
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])#递归构建左子树
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])#递归构建右子树
        return root#返回根节点，递归终止，也就是说递归每次返回的都是根节点，然后根节点的左右子树都会递归构建
    
# @lc code=end

