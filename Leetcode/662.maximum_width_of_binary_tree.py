from typing import Optional
from Leetcode.leetcode import TreeNode

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        levels = []
        ans = 0

        def dfs(node, level, location):
            nonlocal ans

            if not node:
                return

            if len(levels) < level:
                levels.append([location, location])
            else:
                levels[level-1][0] = min(levels[level-1][0], location)
                levels[level-1][1] = max(levels[level-1][1], location)

            #print(level, levels)
            ans = max(ans, levels[level-1][1] - levels[level-1][0] + 1)

            dfs(node.left, level+1, location*2-1)
            dfs(node.right, level+1, location*2)


        dfs(root, 1, 1)

        return ans