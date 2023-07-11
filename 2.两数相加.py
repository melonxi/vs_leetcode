#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化进位为0，dummy节点为0，before_node指向dummy节点
        carry = 0
        dummy = ListNode(0)
        before_node = dummy
        
        # 遍历两个链表，直到两个链表都为空
        while l1 or l2:
            # 如果两个链表都不为空，则将两个节点的值相加，再加上进位
            if l1 and l2:
                node_val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            # 如果l1不为空，l2为空，则将l1节点的值加上进位
            elif l1:
                node_val = l1.val + carry
                l1 = l1.next
            # 如果l2不为空，l1为空，则将l2节点的值加上进位
            elif l2:
                node_val = l2.val + carry
                l2 = l2.next
            
            # 判断相加后的值是否大于等于10，如果是，则进位为1，当前节点的值为相加后的值减去10
            if node_val >= 10:
                carry = 1
                temp_node = ListNode(node_val-10)
            # 如果相加后的值小于10，则进位为0，当前节点的值为相加后的值
            else:
                carry = 0
                temp_node = ListNode(node_val)
            
            # 将当前节点添加到链表中
            before_node.next = temp_node
            before_node = temp_node
        
        # 如果最后还有进位，则在链表末尾添加一个值为1的节点
        if carry:
            before_node.next = ListNode(1)        

        # 返回dummy节点的下一个节点，即为相加后的链表
        return dummy.next
                
# @lc code=end

