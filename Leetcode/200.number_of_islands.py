from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])

        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        visited = set()

        def dfs(node):
            i, j = node[0], node[1]

            visited.add((i,j))

            for d in directions:
                ii, jj = i + d[0], j + d[1]

                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == "1" and (ii,jj) not in visited:
                    dfs((ii,jj))

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    #print((i,j))
                    ans += 1
                    dfs((i,j))

        return ans