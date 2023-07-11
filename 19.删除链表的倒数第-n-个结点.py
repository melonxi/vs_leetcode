#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #快慢指针，设定一个计数器，快指针每走一步，计数器+1，当计数器等于n时，慢指针开始走，当快指针走到最后一个节点时，慢指针的下一个节点就是要删除的节点

        dummy = ListNode(0,head)
        slow,fast = dummy,dummy
        count = 0
        while fast.next:
            fast = fast.next
            count += 1
            if count > n:
                slow = slow.next

        slow.next = slow.next.next
        return dummy.next


    

# @lc code=end

