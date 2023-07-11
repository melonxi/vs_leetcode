#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个哨兵节点，用于最终的结果返回
        dummy = ListNode()
        # 创建一个指针，最开始指针指向哨兵节点
        cur_node = dummy
        # 构建一个循环，通过比较list1和list2的值，确定指针应该指向的下一个节点
        while list1 and list2:
            if list1.val < list2.val:
                cur_node.next = list1
                list1 = list1.next
            else:
                cur_node.next = list2
                list2 = list2.next
            # 每次循环，指针都要向后移动一位
            cur_node = cur_node.next
        # 循环结束后，将剩余的链表接到指针后面
        if list1:
            cur_node.next = list1
        else:
            cur_node.next = list2
        # 返回哨兵节点的下一个节点
        return dummy.next
    
# @lc code=end

