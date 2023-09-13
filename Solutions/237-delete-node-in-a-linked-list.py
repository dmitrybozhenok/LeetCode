# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        next_node = node.next
        node.next = next_node.next
        node.val = next_node.val
