from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        my_set = {head}
        while head.next is not None:
            if my_set.__contains__(head.next):
                return head.next
            my_set.add(head.next)
            head = head.next
        return None