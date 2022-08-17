from typing import Optional
from Leetcode.leetcode import TreeNode

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans = float("-inf")

        def find_path_dfs(node) ->int:
            nonlocal ans

            if not node:
                return 0

            left = find_path_dfs(node.left)
            right = find_path_dfs(node.right)

            # If any path is negative, use 0 in stead
            left = max(left, 0)
            right = max(right, 0)

            # Two posable paths:
            path1 = left + right + node.val
            path2 = max(left, right) + node.val

            ans = max(ans, path1, node.val, path2)

            return path2

        find_path_dfs(root)

        return ans
