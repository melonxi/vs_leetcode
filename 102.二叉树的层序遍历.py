#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #队列+迭代
        '''
        if not root:
            return []
        deq = deque()
        deq.append(root)
        res = []
        while deq:
            cur_lens = len(deq)
            cur_res = []
            for i in range(cur_lens):
                cur_node = deq.popleft()
                cur_res.append(cur_node.val)
                if cur_node.left:
                    deq.append(cur_node.left)
                if cur_node.right:
                    deq.append(cur_node.right) 
            res.append(cur_res)
        return res
        '''
        #BFS递归实现
        res = []
        def bfs(root,level):
            if not root:
                return 
            if len(res) == level:#如果当前层还没有元素，就添加一个空列表
                res.append([])
            res[level].append(root.val)#将当前节点的值加入到对应层的列表中
            bfs(root.left,level+1)#递归的处理下一层
            bfs(root.right,level+1)#递归的处理下一层
        bfs(root,0)
        return res
    
# @lc code=end

