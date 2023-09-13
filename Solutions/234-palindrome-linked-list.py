from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = [head]
        node = head
        while node.next is not None:
            stack.append(node.next)
            node = node.next
        while head.next is not None:
            if stack[-1].val != head.val:
                return False
            stack.pop()
            head = head.next
        return True