#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #hash表法，当前节点为键，下个节点为值
        #遍历链表，当下个节点已经在hash表中，说明有环
        if not head or not head.next:
            return False
        check_dict = {}
        while head:
            if head not in check_dict:
                check_dict[head] = head.next
                head = head.next
            else:
                return True
        return False
        
# @lc code=end

