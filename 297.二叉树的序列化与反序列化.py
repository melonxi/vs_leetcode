#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#双端队列
from collections import deque

class Codec:
    def __init__(self) -> None:
        self.ans = []

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #层序遍历
        if not root:
            return ""
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                self.ans.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                self.ans.append("null")
        return ",".join(self.ans)
    
        


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
            
        #层序遍历，遍历到序列化中的每一个元素，都从队列的右边添加
        #因为是序列化，所以data是一个字符串，首先需要将字符串按照格式分割，也就按照","分割
        if not data:
            return None
        data = data.split(",")
        dq = deque()
        root = TreeNode(int(data[0]))
        dq.append(root)
        #因为第一个元素，也就是根节点，已经被弹出了，所以要从1开始计算索引
        index = 1
        while dq:
            node = dq.popleft()
            if data[index] != "null":
                node.left = TreeNode(int(data[index]))
                dq.append(node.left)
            index += 1
            if data[index] != "null":
                node.right = TreeNode(int(data[index]))
                dq.append(node.right)
            index += 1
        return root
    

    
    




            

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

