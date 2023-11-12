# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        nodes = [head]
        cur = head
        while cur.next:
            nodes.append(cur.next)
            cur = cur.next

        l = head
        r = nodes.pop()
        while l != r:
            lnext = l.next
            if l.next == r:
                break
            l.next = r
            l = lnext
            r.next = l
            r = nodes.pop()
        r.next = None


solution = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
ret = solution.reorderList(node1)


