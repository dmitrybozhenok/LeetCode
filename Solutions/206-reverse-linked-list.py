from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        stack = [head]
        while head.next is not None:
            head = head.next
            stack.append(head)
        ret = head
        while len(stack) > 1:
            node = stack.pop()
            node.next = stack[-1]
        stack[-1].next = None
        return ret