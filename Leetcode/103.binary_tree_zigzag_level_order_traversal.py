from typing import List, Optional
from Leetcode.leetcode import TreeNode

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        from collections import deque

        q = deque()

        q.append((root,0))

        ans = []

        while q:

            node, level = q.popleft()

            if not node:
                continue

            if len(ans) <= level:
                ans.append([])

            if level % 2:
                ans[level].append(node.val)
            else:
                ans[level].insert(0, node.val)

            q.append((node.right, level+1))
            q.append((node.left, level+1))

        return ans