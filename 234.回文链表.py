#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. 快慢指针找到中点
        # 2. 反转后半部分
        # 3. 比较前后两部分
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        # slow指向中点
        # 反转后半部分
        pre, cur = None, slow.next  
        while cur:
            #cur.next, pre, cur = pre, cur, cur.next
            next_node = cur.next  # 存储下一个节点
            cur.next = pre  # 反转指向
            pre = cur  # 更新已经反转的链表的头节点
            cur = next_node  # 更新待反转的链表的头节点

        # pre指向反转后的头结点
        # 比较前后两部分    
        while pre:
            if pre.val != head.val:
                return False
            pre, head = pre.next, head.next
        return True
    
# @lc code=end

