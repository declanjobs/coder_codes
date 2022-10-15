from typing import Optional
from Leetcode.leetcode import TreeNode

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        from collections import defaultdict
        ans = 0

        def dfs(node, prefix_sum: int, prefix_sum_lookup: defaultdict):
            nonlocal ans, targetSum

            if not node:
                return

            prefix_sum += node.val

            if (prefix_sum - targetSum) in prefix_sum_lookup\
                or prefix_sum == targetSum:
                #print(prefix_sum_lookup)
                ans += prefix_sum_lookup[prefix_sum - targetSum]

            prefix_sum_lookup[prefix_sum] += 1

            dfs(node.left, prefix_sum, prefix_sum_lookup)
            dfs(node.right, prefix_sum, prefix_sum_lookup)

            prefix_sum_lookup[prefix_sum] -= 1
            if prefix_sum_lookup[prefix_sum] == 0:
                del prefix_sum_lookup[prefix_sum]

            prefix_sum -= node.val

        prefix_sum_lookup = defaultdict(int)
        prefix_sum_lookup[0] = 1
        dfs(root, 0, prefix_sum_lookup)

        return ans