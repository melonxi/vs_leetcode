#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #双指针A，B.
        #指针A,B以相同速度遍历链表，走完当前链表就去遍历另一个链表，这样两个指针走的路程相同，如果有相交节点，就会在相交节点相遇
        #如果没有相交节点，就会在None处相遇
        if not headA or not headB:
            return None
        tempA = headA
        tempB = headB
        while tempA!=tempB:
            tempA = tempA.next if tempA else headB
            tempB = tempB.next if tempB else headA
        return tempA
    
        
# @lc code=end

