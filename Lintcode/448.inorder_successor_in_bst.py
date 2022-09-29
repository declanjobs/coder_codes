from Lintcode.lintcode import TreeNode
from typing import Optional


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root: Optional[TreeNode], p: Optional[TreeNode]):
        # write your code here
        successor = None
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor