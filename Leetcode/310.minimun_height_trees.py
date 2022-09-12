class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        from collections import defaultdict

        tree = defaultdict(set)

        for e in edges:
            tree[e[0]].add(e[1])
            tree[e[1]].add(e[0])

        #print(tree)
        leaves = []
        for node in range(n):
            if len(tree[node]) == 1:
                leaves.append(node)

        leaves_remain = n
        while leaves_remain > 2:

            leaves_remain -= len(leaves)
            new_leaves = []

            while leaves:

                leaf = leaves.pop()
                neighbor = tree[leaf].pop()
                tree[neighbor].remove(leaf)

                if len(tree[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves


        return leaves