from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        if not cur:
            return None
        copyhead = Node(cur.val)
        copymap = {head: copyhead}
        copycur = copyhead
        while cur.next:
            copycur.next = Node(cur.next.val)
            copymap[cur.next] = copycur.next
            cur = cur.next
            copycur = copycur.next

        cur = head
        while cur.next:
            copycur = copymap[cur]
            copycur.next = copymap[cur.next]
            if cur.random is not None:
                copycur.random = copymap[cur.random]
            cur = cur.next
        copycur = copymap[cur]
        if cur.random is not None:
                copycur.random = copymap[cur.random]
        return copyhead
