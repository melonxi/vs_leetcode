#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #新建一个不带random的链表，将原链表的每个节点复制一份，且构建一个哈希表，key为原链表节点，value为新链表节点
        #再次遍历原链表，将新链表的random指针指向哈希表中对应的节点
        #时间复杂度O(n)
        #空间复杂度O(n)
        if not head:
            return None
        #新建一个不带random的链表
        dummy = Node(0)
        cur = dummy
        or_head = head
        #构建一个哈希表，key为原链表节点，value为新链表节点
        hashmap = {}
        while head:
            node = Node(head.val)
            cur.next = node
            cur = cur.next
            hashmap[head] = node
            head = head.next
        #再次遍历原链表，将新链表的random指针指向哈希表中对应的节点
        cur = dummy.next
        head = or_head
        while head:
            if head.random:
                cur.random = hashmap[head.random]
            head = head.next
            cur = cur.next
        return dummy.next
    
        
# @lc code=end

