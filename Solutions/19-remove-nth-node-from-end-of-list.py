from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return
        ret = head
        stack = [head]
        while head.next is not None:
            head = head.next
            stack.append(head)
        if len(stack) == n:
            return ret.next
        elif n == 1:
            stack[-2].next = None
        else:
            stack[-n-1].next = stack[-n+1]
        return ret