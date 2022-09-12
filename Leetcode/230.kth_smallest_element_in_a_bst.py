from typing import Optional
from Leetcode.leetcode import TreeNode


class Solution:

    # In-order traversal of BST is an array sorted in the ascending order.
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        while stack or root:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            k -= 1
            if k == 0:
                return root.val

            root = root.right