from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        l3 = ListNode(0)
        ret = l3
        while l1 or l2 or rem:
            sum = rem
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            num = sum % 10
            rem = sum // 10
            l3.val = num
            if l1 or l2 or rem:
                l3.next = ListNode(0)
                l3 = l3.next
        return ret