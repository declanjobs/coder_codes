from typing import List
from Leetcode.leetcode import TreeNode

# Convert Tree to Graph first
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        from collections import defaultdict

        graph = defaultdict(set)

        def dfs_tree_to_graph(node):
            if node.left:
                graph[node].add(node.left)
                graph[node.left].add(node)
                dfs_tree_to_graph(node.left)

            if node.right:
                graph[node].add(node.right)
                graph[node.right].add(node)
                dfs_tree_to_graph(node.right)

        dfs_tree_to_graph(root)

        ans = []
        visited = set()
        def dfs_find_ans(node, dist):
            if not node:
                return

            visited.add(node)
            if dist == k:
                ans.append(node.val)
                return

            for n in graph[node]:
                if n not in visited:
                    dfs_find_ans(n, dist+1)

        dfs_find_ans(target, 0)

        return ans