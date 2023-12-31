import queue
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        q = [root]
        output = []
        while q:
            node = q.pop()
            output.append(node.val)
            for c in reversed(node.children):
                q.append(c)
        return output