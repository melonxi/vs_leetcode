#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #使用归并排序的思想
        #所谓归并排序，就是利用分治的思想，将链表分为两部分，然后分别对两部分进行排序，最后将两部分合并
        #归并排序的时间复杂度为O(nlogn)，空间复杂度为O(logn)
        def merge(left,right):
            dummy = ListNoteBook()
            cur = dummy
            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next#注意这里要更新cur
            if left:
                cur.next = left
            if right:
                cur.next = right
            return dummy.next
        #递归的终止条件
        if not head or not head.next:
            return head
        #快慢指针找到链表的中点
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #将链表分为两部分
        right = slow.next
        slow.next = None#断开链表
        #递归的对两部分进行排序
        left = self.sortList(head)
        right = self.sortList(right)
        #合并两部分
        return merge(left,right)
    """
    

                    
# @lc code=end

