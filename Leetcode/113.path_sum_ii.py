from typing import List, Optional
from Leetcode.leetcode import TreeNode

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:


        ans = []

        def dfs(node, path: list, pathSum: int):

            if not node:
                return

            path.append(node.val)
            pathSum += node.val

            if not node.left and not node.right and pathSum == targetSum:
                ans.append(list(path))
                #return

            dfs(node.left, path, pathSum)
            dfs(node.right, path, pathSum)

            path.pop()
            pathSum -= node.val

        dfs(root, [], 0)

        return ans