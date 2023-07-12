#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #小顶堆,左边为优先级，右边为元素
        #时间复杂度O(NlogK),N为所有链表节点数，K为链表数
        hq = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(hq,(lists[i].val,i))
                lists[i] = lists[i].next
        dummy = ListNode()
        cur = dummy
        while hq:
            val,idx = heapq.heappop(hq)     
            cur.next = ListNode(val)
            cur = cur.next
            if lists[idx]:
                heapq.heappush(hq,(lists[idx].val,idx))
                lists[idx] = lists[idx].next
        return dummy.next

# @lc code=end

