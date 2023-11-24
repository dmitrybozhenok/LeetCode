# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTreeInner(self, root) -> TreeNode:
        tmp = root.left
        root.left = root.right
        root.right = tmp
        if root.left:
            self.invertTreeInner(root.left)
        if root.right:
            self.invertTreeInner(root.right)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.invertTreeInner(root)
        return root



